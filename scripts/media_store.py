"""Resolve immutable reference media without bundling it in the skill."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import ssl
import subprocess
import tempfile
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent


def load_manifest(root=ROOT):
    return json.loads((root / 'references/media-manifest.json').read_text())


def cache_root(manifest):
    base = Path(os.environ.get('UI_ATLAS_CACHE_DIR',
                str(Path(os.environ.get('XDG_CACHE_HOME', str(Path.home() / '.cache')))
                    / 'ui-atlas'))).expanduser()
    return base / manifest['revision']


def checked_path(value):
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or not path.parts or path.parts[0] != 'assets':
        raise ValueError(f'Invalid media path: {value}')
    return path


def media_url(manifest, value):
    checked_path(value)
    return manifest['base_url'].rstrip('/') + '/' + value


def matches(path, record):
    return (path.is_file() and path.stat().st_size == record['bytes']
            and hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'])


def local_media(manifest, value, root=ROOT):
    checked_path(value)
    record = manifest['files'][value]
    for path in (root / value, cache_root(manifest) / value):
        if matches(path, record):
            return path
    return None


def fetch(manifest, value, root=ROOT):
    existing = local_media(manifest, value, root)
    if existing:
        return existing
    record = manifest['files'][value]
    destination = cache_root(manifest) / checked_path(value)
    destination.parent.mkdir(parents=True, exist_ok=True)
    url = media_url(manifest, value)
    fd, name = tempfile.mkstemp(prefix='.download-', dir=destination.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'ui-atlas-media/1'})
            with urllib.request.urlopen(request, timeout=30) as response, temporary.open('wb') as output:
                shutil.copyfileobj(response, output)
        except urllib.error.URLError as error:
            # Some Python distributions lack the OS CA bundle. curl still verifies TLS.
            if not isinstance(error.reason, ssl.SSLCertVerificationError) or not shutil.which('curl'):
                raise
            subprocess.run(['curl', '--fail', '--location', '--silent', '--show-error',
                            '--max-time', '60', '--output', str(temporary), url], check=True)
        if not matches(temporary, record):
            raise ValueError(f'Media checksum or size mismatch: {value}')
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)
    return destination


def entry_media(entry, selection='preview'):
    kind = entry.get('media_type')
    if kind == 'recipe':
        return []
    if kind == 'gallery':
        if selection == 'preview':
            return [entry['preview']]
        if selection in {'images', 'all'}:
            return ([entry['preview']] if selection == 'all' else []) + entry['images']
        raise ValueError('Gallery media accepts preview, images or all')
    if kind in {'animation', 'filmstrip'}:
        if selection in {'preview', 'images'}:
            return [entry['filmstrip']]
        if selection in {'gif', 'all'}:
            if kind == 'animation':
                return ([entry['filmstrip']] if selection == 'all' else []) + [entry['gif']]
            if selection == 'all':
                return [entry['filmstrip']]
            raise ValueError('该条目仅保留 JPG，没有 GIF；请使用 --media preview 或 images')
        raise ValueError('Reference media accepts preview, images, gif or all')
    raise ValueError(f'Unknown media type: {kind}')
