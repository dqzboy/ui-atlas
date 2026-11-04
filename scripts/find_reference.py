#!/usr/bin/env python3
"""Search the bundled UI reference index. Uses only the Python standard library."""
import argparse
import json
from pathlib import Path

from media_store import load_manifest, local_media, media_url
from detail_media import load_quality, detail_paths


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
    quality = load_quality(root)
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
            print(f"  效果图: {local_media(manifest, entry['preview'], root) or root / entry['preview']}")
            if entry.get('gif'):
                print(f"  动图: {local_media(manifest, entry['gif'], root) or root / entry['gif']}")
            print('  证据: 演示画面抽帧与精选片段；配方参数仍需在实际项目中验证。')
        elif entry.get('media_type') == 'gallery':
            print(f"  媒体: 静态图集（{len(entry['images'])} 张，不代表交互状态）")
            poster = detail_paths(entry['id'], 'preview', root, quality)
            if poster:
                print(f"  原尺寸效果图: {poster[0]}")
            print(f"  总览: {local_media(manifest, entry['preview'], root) or media_url(manifest, entry['preview'])}")
            for number, path in enumerate(entry['images'], 1):
                print(f"  图片 {number:02}: {local_media(manifest, path, root) or media_url(manifest, path)}")
        else:
            poster = detail_paths(entry['id'], 'preview', root, quality)
            if poster:
                print(f"  原尺寸效果图: {poster[0]}")
            print(f"  六帧图: {local_media(manifest, entry['filmstrip'], root) or media_url(manifest, entry['filmstrip'])}")
            if entry.get('media_type') == 'animation':
                print(f"  GIF: {local_media(manifest, entry['gif'], root) or media_url(manifest, entry['gif'])}")
                print(f"  按需获取动图: python3 scripts/fetch_media.py {entry['id']} --media gif")
            else:
                print('  证据: 抽样状态图片；不能证明连续运动与短暂状态。')
        if entry.get('media_reason'):
            print(f"  媒体取舍: {entry['media_reason']}")
        detail = quality['entries'].get(entry['id'])
        if detail:
            print(f"  清晰度边界: {detail['limitation']}")
            for selection, label in [('images', '独立细节图'), ('gif', '清晰动图')]:
                paths = detail_paths(entry['id'], selection, root, quality)
                if paths:
                    print(f"  {label}: " + '\n    '.join(str(p) for p in paths))
            if detail.get('images'):
                print(f"  读取独立图: python3 scripts/fetch_media.py {entry['id']} --media images")
        if entry.get('media_type') != 'recipe':
            print(f"  按需获取预览: python3 scripts/fetch_media.py {entry['id']}")
        if entry.get('related'):
            print('  相关: ' + ', '.join(entry['related']))
        print()


if __name__ == '__main__':
    main()
