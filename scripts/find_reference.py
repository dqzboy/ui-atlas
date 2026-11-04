#!/usr/bin/env python3
"""Search the bundled UI reference index. Uses only the Python standard library."""
import argparse
import json
from pathlib import Path

from media_store import load_manifest, local_media, media_url


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--id', dest='entry_id')
    parser.add_argument('--category', help='分类 ID，例如 dashboard-layouts')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    data = json.loads((root / 'references/catalog.json').read_text())
    manifest = load_manifest(root)
    categories = {category['id'] for category in data['categories']}
    if args.category and args.category not in categories:
        parser.error('未知分类；可选分类：' + ', '.join(sorted(categories)))

    words = args.query.strip().casefold().split()
    items = []
    for entry in data['items']:
        if args.category and entry['category'] != args.category:
            continue
        if args.entry_id and entry['id'] != args.entry_id:
            continue
        fields = [entry[key] for key in
                  ('id', 'name', 'english', 'summary', 'prompt', 'category_title')]
        fields.extend(entry.get('keywords', []))
        searchable = ' '.join(fields).casefold()
        if all(word in searchable for word in words):
            items.append(entry)

    if args.json:
        print(json.dumps(items, ensure_ascii=False, indent=2))
        return
    if not items:
        parser.exit(1, '未找到匹配条目，请换用分类或中英文名称。\n')
    for entry in items:
        print(f"{entry['id']} | {entry['name']} / {entry['english']}")
        print(f"  要点: {entry['summary']}\n  例句: {entry['prompt']}")
        print(f"  说明: {root}/references/{entry['category']}.md#{entry['slug']}")
        if entry.get('media_type') == 'recipe':
            print(f"  配方: {root / entry['recipe']}")
            print('  证据: 文字实现配方；未附视觉媒体，不代表效果已验证。')
        elif entry.get('media_type') == 'gallery':
            print(f"  媒体: 静态图集（{len(entry['images'])} 张，不代表交互状态）")
            print(f"  总览: {local_media(manifest, entry['preview'], root) or media_url(manifest, entry['preview'])}")
            for number, path in enumerate(entry['images'], 1):
                print(f"  图片 {number:02}: {local_media(manifest, path, root) or media_url(manifest, path)}")
        else:
            print(f"  六帧图: {local_media(manifest, entry['filmstrip'], root) or media_url(manifest, entry['filmstrip'])}")
            if entry.get('media_type') == 'animation':
                print(f"  GIF: {local_media(manifest, entry['gif'], root) or media_url(manifest, entry['gif'])}")
                print(f"  按需获取动图: python3 scripts/fetch_media.py {entry['id']} --media gif")
            else:
                print('  证据: 抽样状态图片；不能证明连续运动与短暂状态。')
        if entry.get('media_reason'):
            print(f"  媒体取舍: {entry['media_reason']}")
        if entry.get('media_type') != 'recipe':
            print(f"  按需获取预览: python3 scripts/fetch_media.py {entry['id']}")
        if entry.get('related'):
            print('  相关: ' + ', '.join(entry['related']))
        print()


if __name__ == '__main__':
    main()
