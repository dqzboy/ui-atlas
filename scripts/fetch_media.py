#!/usr/bin/env python3
"""Download only the selected reference media; verify SHA-256 and reuse cache."""
import argparse
import json
from pathlib import Path
import sys
import subprocess

from media_store import ROOT, entry_media, fetch, load_manifest, media_url
from detail_media import detail_values, load_quality


def selected_media(entry, selection, manifest, quality):
    """Prefer native references in every edition; select before downloading."""
    details = detail_values(entry['id'], selection, quality)
    if details and selection != 'all':
        return [(quality, value) for value in details]
    originals = entry_media(entry, selection)
    sources = {value: source for source, value in
               [(manifest, value) for value in originals] + [(quality, value) for value in details]}
    return [(source, value) for value, source in sources.items()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entry_id', nargs='?', help='例如 motion/border-beam')
    parser.add_argument('--media', choices=['preview', 'images', 'gif', 'all'], default='preview',
                        help='preview 取一张原尺寸代表图；images 取精选独立图片；all 取条目全部图片')
    parser.add_argument('--all', action='store_true', help='获取当前参考库全部图片并缓存，包括原尺寸参考')
    parser.add_argument('--urls', action='store_true', help='只列出地址，不下载')
    args = parser.parse_args()
    data = json.loads((ROOT / 'references/catalog.json').read_text())
    if args.all and args.entry_id:
        parser.error('--all 不能与条目 ID 同时使用')
    entries = data['items'] if args.all else [e for e in data['items'] if e['id'] == args.entry_id]
    if not entries:
        parser.error('请提供有效条目 ID 或 --all')
    manifest = load_manifest()
    try:
        quality = load_quality()
        for entry in entries:
            selection = 'all' if args.all else args.media
            for source, value in selected_media(entry, selection, manifest, quality):
                if args.urls and not source['files'][value].get('bundled'):
                    print(media_url(source, value))
                else:
                    print(fetch(source, value))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f'媒体获取失败：{error}；文字索引仍可使用，请稍后重试。', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
