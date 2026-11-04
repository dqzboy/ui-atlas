#!/usr/bin/env python3
"""Build a reproducible skill ZIP with declared compact recipe media."""
from pathlib import Path
import argparse
import zipfile

from validate_library import validate
from media_store import load_manifest, local_media
from detail_media import load_quality, validate_quality
from reference_docs import lightweight_document


def main():
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--with-media', action='store_true', help='生成含完整参考与原尺寸细节的离线包')
    args = parser.parse_args()
    catalog, errors = validate(root)
    if errors:
        raise SystemExit('\n'.join(errors))
    paths = [root / 'SKILL.md', root / 'README.md']
    for folder in ('agents', 'references', 'scripts'):
        paths.extend(p for p in (root / folder).rglob('*')
                     if p.is_file() and p.suffix in {'.md', '.json', '.py', '.yaml', '.yml'}
                     and '__pycache__' not in p.parts)
    total = sum(p.stat().st_size for p in paths)
    if total > 2 * 1024 * 1024:
        raise SystemExit('Core skill exceeds 2 MiB; inspect unexpected bundled content.')
    bundled = [root / p for p, record in load_manifest(root)['files'].items()
               if record.get('bundled')]
    if sum(p.stat().st_size for p in bundled) > 8 * 1024 * 1024:
        raise SystemExit('Bundled recipe media exceeds 8 MiB; reduce previews or clips.')
    members = [(path, path.relative_to(root).as_posix()) for path in paths + bundled]
    if args.with_media:
        quality_errors = validate_quality(root, check_files=True)
        if quality_errors:
            raise SystemExit('\n'.join(quality_errors))
        manifest = load_manifest(root)
        for value, record in manifest['files'].items():
            if record.get('bundled'):
                continue
            path = local_media(manifest, value, root)
            if path is None:
                raise SystemExit(f'Missing {value}; run fetch_media.py --all first.')
            members.append((path, value))
        members.extend((root / value, value) for value in load_quality(root)['files'])
    total = 0
    destination = root / ('dist/ui-atlas-offline.zip' if args.with_media else 'dist/ui-atlas.zip')
    destination.parent.mkdir(exist_ok=True)
    manifest, quality = load_manifest(root), load_quality(root)
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, relative in sorted(members, key=lambda item: item[1]):
            info = zipfile.ZipInfo('ui-atlas/' + relative, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            payload = path.read_bytes()
            if not args.with_media and path.suffix == '.md':
                payload = lightweight_document(payload.decode(), catalog['items'], manifest, quality).encode()
            archive.writestr(info, payload)
            total += len(payload)
    print(f'{destination}\n{len(members)} files; {total:,} bytes unpacked; {destination.stat().st_size:,} bytes ZIP')


if __name__ == '__main__':
    main()
