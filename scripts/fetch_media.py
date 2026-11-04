#!/usr/bin/env python3
"""Download only the selected reference media; verify SHA-256 and reuse cache."""
import argparse
import json
from pathlib import Path
import sys
import subprocess

from media_store import ROOT, entry_media, fetch, load_manifest, media_url
from detail_media import detail_paths, load_quality


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entry_id', nargs='?', help='例如 motion/border-beam')
    parser.add_argument('--media', choices=['preview', 'images', 'gif', 'all'], default='preview',
                        help='preview 优先取原尺寸代表图；images 取独立图片；gif 优先取清晰版本')
    parser.add_argument('--all', action='store_true', help='获取全部原有公开媒体；独立细节图随完整版本提供')
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
            details = [] if args.urls else detail_paths(entry['id'], selection, quality=quality)
            if details and selection in {'preview', 'images', 'gif'}:
                for path in details:
                    print(path)
                continue
            paths = entry_media(entry, selection)
            if (not args.urls and selection == 'images' and not details
                    and entry['media_type'] in {'animation', 'filmstrip'}):
                print('原尺寸独立帧尚未安装，以下为六帧总览；细节判断请使用完整媒体包。', file=sys.stderr)
            if (not args.urls and selection == 'gif' and not details
                    and quality['entries'].get(entry['id'], {}).get('gif')):
                print('大尺寸动图尚未安装，以下为精简动图；清晰版本见完整媒体包。', file=sys.stderr)
            if not paths:
                print(f"{entry['id']}: 文字配方，见 {ROOT / entry['recipe']}")
            for value in paths:
                if args.urls and not manifest['files'][value].get('bundled'):
                    print(media_url(manifest, value))
                else:
                    print(fetch(manifest, value))
            for path in details:
                print(path)
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f'媒体获取失败：{error}；文字索引仍可使用，请稍后重试。', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
