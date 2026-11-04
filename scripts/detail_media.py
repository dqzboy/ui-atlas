"""Resolve optional full-size references without replacing immutable originals."""
import json
import re
import struct

from media_store import ROOT, checked_path, local_media, media_url


def load_quality(root=ROOT):
    path = root / 'references/media-quality.json'
    return json.loads(path.read_text()) if path.is_file() else {'entries': {}, 'files': {}}


def image_dimensions(header):
    """Read dimensions from supported still headers without imaging dependencies."""
    if header.startswith(b'\x89PNG\r\n\x1a\n') and len(header) >= 24:
        return struct.unpack('>II', header[16:24])
    if header.startswith((b'GIF87a', b'GIF89a')) and len(header) >= 10:
        return struct.unpack('<HH', header[6:10])
    if len(header) >= 30 and header[:4] == b'RIFF' and header[8:12] == b'WEBP':
        kind = header[12:16]
        if kind == b'VP8X':
            return tuple(1 + int.from_bytes(header[p:p+3], 'little') for p in (24, 27))
        if kind == b'VP8 ' and header[23:26] == b'\x9d\x01\x2a':
            return tuple(n & 0x3fff for n in struct.unpack('<HH', header[26:30]))
        if kind == b'VP8L' and header[20] == 0x2f:
            bits = int.from_bytes(header[21:25], 'little')
            return (1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff))
    raise ValueError('invalid or unsupported image header')


def detail_values(entry_id, selection, quality):
    """Select reference paths without reading or downloading any media."""
    entry = quality['entries'].get(entry_id, {})
    if selection == 'preview':
        values = [entry['poster']] if entry.get('poster') else []
    elif selection == 'images':
        values = entry.get('images', [])
    elif selection == 'gif':
        values = [entry['gif']] if entry.get('gif') else []
    elif selection == 'all':
        values = entry.get('images', []) + ([entry['gif']] if entry.get('gif') else [])
    else:
        return []
    for value in values:
        relative = checked_path(value)
        if not relative.as_posix().startswith('assets/details/'):
            raise ValueError(f'Invalid detail media path: {value}')
    return values


def detail_paths(entry_id, selection, root=ROOT, quality=None):
    """Return a verified selection from the install or external cache."""
    quality = load_quality(root) if quality is None else quality
    paths = []
    for value in detail_values(entry_id, selection, quality):
        path = local_media(quality, value, root)
        if path is None:
            return []
        paths.append(path)
    return paths


def validate_quality(root=ROOT, check_files=False, check_links=True):
    quality = load_quality(root)
    errors, used = [], set()
    catalog = json.loads((root / 'references/catalog.json').read_text())
    entries = {e['id']: e for e in catalog['items']}
    base = json.loads((root / 'references/media-manifest.json').read_text())
    if quality.get('base_revision') != base['revision']:
        errors.append('Detail media base revision mismatch')
    revision = quality.get('revision', '')
    if (not re.fullmatch(r'[0-9a-f]{40}', revision)
            or quality.get('base_url') != 'https://raw.githubusercontent.com/dqzboy/ui-atlas/' + revision):
        errors.append('Detail media origin must use an immutable published revision')
    for entry_id, entry in quality['entries'].items():
        if entry_id not in entries:
            errors.append(f'Unknown detail entry: {entry_id}')
            continue
        if not entry.get('source') or not entry.get('limitation'):
            errors.append(f'Missing detail source or limitation: {entry_id}')
        if entry.get('gif') and not entries[entry_id].get('gif'):
            errors.append(f'Detail GIF contradicts media selection: {entry_id}')
        if entry.get('images') and entry.get('poster') not in entry['images']:
            errors.append(f'Detail poster must reference an independent image: {entry_id}')
        values = entry.get('images', []) + ([entry['gif']] if entry.get('gif') else [])
        if not values:
            errors.append(f'Empty detail entry: {entry_id}')
        for value in values:
            try:
                path = checked_path(value)
                record = quality['files'][value]
                if not value.startswith('assets/details/') or path.suffix not in {'.png', '.gif', '.webp'}:
                    raise ValueError('unsupported path or format')
                if not all(isinstance(record.get(k), int) and record[k] > 0
                           for k in ('bytes', 'width', 'height')):
                    raise ValueError('invalid size or dimensions')
                if not re.fullmatch('[0-9a-f]{64}', record.get('sha256', '')):
                    raise ValueError('invalid hash')
                used.add(value)
                if check_files:
                    local = local_media(quality, value, root)
                    if local is None:
                        raise ValueError('missing or corrupt local file')
                    with local.open('rb') as media:
                        header = media.read(32)
                    size = image_dimensions(header)
                    if size != (record['width'], record['height']):
                        raise ValueError('pixel dimensions mismatch')
            except (OSError, ValueError, KeyError) as error:
                errors.append(f'{entry_id}: {value}: {error}')
    for value in set(quality['files']) - used:
        errors.append(f'Unreferenced detail file: {value}')
    if check_files:
        installed = {p.relative_to(root).as_posix()
                     for p in (root / 'assets/details').rglob('*')
                     if p.is_file() and p.suffix in {'.png', '.gif', '.webp'}}
        for value in sorted(installed - set(quality['files'])):
            errors.append(f'Unlisted detail file: {value}')
    # Both editions retain the full references; only the link location differs.
    if check_links:
        for entry_id, detail in quality['entries'].items():
            if entry_id not in entries:
                continue
            document = root / 'references' / (entries[entry_id]['category'] + '.md')
            if not document.is_file():
                continue
            text = document.read_text()
            block = re.search(r'<!-- ui-atlas:details ' + re.escape(entry_id)
                              + r' -->\n(.*?)<!-- /ui-atlas:details -->', text, re.S)
            if not block:
                errors.append(f'Missing attached detail references: {entry_id}')
                continue
            gif = detail.get('gif') or entries[entry_id].get('gif')
            for value in detail.get('images', []) + ([gif] if gif else []):
                source = quality if value in quality['files'] else base
                targets = ['../' + value]
                if not source['files'][value].get('bundled'):
                    targets.append(media_url(source, value))
                if not any(f']({target})' in block[1] for target in targets):
                    errors.append(f'Missing matching detail link: {entry_id}: {value}')
            poster = detail.get('poster')
            targets = ['../' + poster] if poster else []
            if poster and not quality['files'][poster].get('bundled'):
                targets.append(media_url(quality, poster))
            if poster and not any(re.search(r'!\[[^\n]*\]\(' + re.escape(target) + r'\)', block[1])
                                  for target in targets):
                errors.append(f'Missing full-size inline reference: {entry_id}')
    return errors
