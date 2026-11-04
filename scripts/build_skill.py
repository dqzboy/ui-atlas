#!/usr/bin/env python3
"""Build a small, reproducible skill ZIP without media or repository history."""
from pathlib import Path
import zipfile

from validate_library import validate


def main():
    root = Path(__file__).resolve().parent.parent
    _, errors = validate(root)
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
    destination = root / 'dist/ui-atlas.zip'
    destination.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(paths):
            info = zipfile.ZipInfo('ui-atlas/' + path.relative_to(root).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print(f'{destination}\n{len(paths)} files; {total:,} bytes unpacked; {destination.stat().st_size:,} bytes ZIP')


if __name__ == '__main__':
    main()
