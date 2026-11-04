#!/usr/bin/env python3
"""Download only the selected reference media; verify SHA-256 and reuse cache."""
import argparse
import json
from pathlib import Path
import sys
import subprocess

from media_store import ROOT, entry_media, fetch, load_manifest, media_url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entry_id', nargs='?', help='例如 motion/border-beam')
    parser.add_argument('--media', choices=['preview', 'images', 'gif', 'all'], default='preview',
                        help='默认只取 JPG；gif 仅适用于保留动态参考的条目')
    parser.add_argument('--all', action='store_true', help='下载完整媒体库，供离线使用')
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
        for entry in entries:
            paths = entry_media(entry, 'all' if args.all else args.media)
            if not paths:
                print(f"{entry['id']}: 文字配方，见 {ROOT / entry['recipe']}")
            for value in paths:
                print(media_url(manifest, value) if args.urls else fetch(manifest, value))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f'媒体获取失败：{error}；文字索引仍可使用，请稍后重试。', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
