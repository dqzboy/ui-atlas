#!/usr/bin/env python3
"""Restore reviewed media and attach full-size evidence to the matching entries."""
import argparse
import json
import re
import shutil

from detail_media import load_quality, validate_quality
from media_store import ROOT, load_manifest, local_media, matches
from reference_docs import DETAIL_BLOCK, lightweight_document


def sync(root=ROOT, restore=False):
    data = json.loads((root / 'references/catalog.json').read_text())
    manifest, quality = load_manifest(root), load_quality(root)
    if restore:
        for value, record in manifest['files'].items():
            target = root / value
            if matches(target, record):
                continue
            source = local_media(manifest, value, root)
            if source is None:
                raise FileNotFoundError(f'No verified source for {value}; run fetch_media.py --all')
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    errors = validate_quality(root, check_files=False, check_links=False)
    if errors:
        raise ValueError('\n'.join(errors))
    for category in data['categories']:
        document = root / 'references' / (category['id'] + '.md')
        text = document.read_text()
        text = text.replace(manifest['base_url'].rstrip('/') + '/', '../')
        for entry in [e for e in data['items'] if e['category'] == category['id']]:
            detail = quality['entries'].get(entry['id'])
            if not detail:
                continue
            pattern = re.compile(r'(<a id="' + re.escape(entry['slug'])
                                 + r'"></a>\n)(.*?)(?=\n<a id=|\Z)', re.S)
            match = pattern.search(text)
            if not match:
                raise ValueError(f'Missing section: {entry["id"]}')
            body = DETAIL_BLOCK.sub('', match[2]).rstrip()
            # A small overview stays linked for state comparison; the inline
            # image is now the independent full-size reference.
            if detail.get('images'):
                body = re.sub(r'\n!\[[^\n]*\]\(\.\./assets/[^)]+\)\n?', '\n', body).rstrip()
            lines = [f'<!-- ui-atlas:details {entry["id"]} -->']
            if detail.get('images'):
                links = []
                for number, value in enumerate(detail['images'], 1):
                    record = quality['files'][value]
                    links.append(f'[{number:02} · {record["width"]}×{record["height"]}](../{value})')
                lines.append('- 原尺寸图片：' + ' · '.join(links) + '。')
                if len(detail['images']) > 1 and detail.get('image_reason'):
                    lines.append('- 多图用途：' + detail['image_reason'])
            lines.append('- 清晰度边界：' + detail['limitation'])
            if detail.get('poster'):
                lines += ['', f'![{entry["name"]}：原尺寸独立参考](../{detail["poster"]})']
            lines.append('<!-- /ui-atlas:details -->')
            body += '\n\n' + '\n'.join(lines) + '\n'
            text = text[:match.start(2)] + body + text[match.end(2):]
        document.write_text(lightweight_document(text.rstrip() + '\n', data['items'], manifest, quality))

    return len(quality['entries'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--restore', action='store_true', help='从已校验缓存恢复原有媒体到项目')
    print(f'Synchronized {sync(restore=parser.parse_args().restore)} reference sections.')
