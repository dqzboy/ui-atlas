"""Resolve optional full-size references without replacing immutable originals."""
import json
import re
import struct

from media_store import ROOT, checked_path, matches


def load_quality(root=ROOT):
    path = root / 'references/media-quality.json'
    return json.loads(path.read_text()) if path.is_file() else {'entries': {}, 'files': {}}


def detail_paths(entry_id, selection, root=ROOT, quality=None):
    """Return a complete, verified local selection, or nothing for a fallback."""
    quality = load_quality(root) if quality is None else quality
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
    paths = []
    for value in values:
        relative = checked_path(value)
        if not relative.as_posix().startswith('assets/details/'):
            raise ValueError(f'Invalid detail media path: {value}')
        path = root / relative
        if not matches(path, quality['files'][value]):
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
                if not value.startswith('assets/details/') or path.suffix not in {'.png', '.gif'}:
                    raise ValueError('unsupported path or format')
                if not all(isinstance(record.get(k), int) and record[k] > 0
                           for k in ('bytes', 'width', 'height')):
                    raise ValueError('invalid size or dimensions')
                if not re.fullmatch('[0-9a-f]{64}', record.get('sha256', '')):
                    raise ValueError('invalid hash')
                used.add(value)
                if check_files:
                    local = root / path
                    if not matches(local, record):
                        raise ValueError('missing or corrupt local file')
                    with local.open('rb') as media:
                        header = media.read(24)
                    signatures = (b'\x89PNG\r\n\x1a\n',) if path.suffix == '.png' else (b'GIF87a', b'GIF89a')
                    minimum = 24 if path.suffix == '.png' else 10
                    if len(header) < minimum or not header.startswith(signatures):
                        raise ValueError('invalid file header')
                    size = (struct.unpack('>II', header[16:24]) if path.suffix == '.png'
                            else struct.unpack('<HH', header[6:10]))
                    if size != (record['width'], record['height']):
                        raise ValueError('pixel dimensions mismatch')
            except (OSError, ValueError, KeyError) as error:
                errors.append(f'{entry_id}: {value}: {error}')
    for value in set(quality['files']) - used:
        errors.append(f'Unreferenced detail file: {value}')
    if check_files:
        installed = {p.relative_to(root).as_posix()
                     for p in (root / 'assets/details').rglob('*')
                     if p.is_file() and p.suffix in {'.png', '.gif'}}
        for value in sorted(installed - set(quality['files'])):
            errors.append(f'Unlisted detail file: {value}')
    # Complete editions must actually attach the media to its matching section;
    # lightweight editions intentionally omit the detail directory and blocks.
    if check_links and (root / 'assets/details').is_dir():
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
                if f'](../{value})' not in block[1]:
                    errors.append(f'Missing matching detail link: {entry_id}: {value}')
            poster = detail.get('poster')
            if poster and not re.search(r'!\[[^\n]*\]\(\.\./' + re.escape(poster) + r'\)', block[1]):
                errors.append(f'Missing full-size inline reference: {entry_id}')
    return errors
