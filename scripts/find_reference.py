#!/usr/bin/env python3
"""Search the bundled UI reference index. Uses only the Python standard library."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--id', dest='entry_id')
    parser.add_argument('--category', help='分类 ID，例如 dashboard-layouts')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    data = json.loads((root / 'references/catalog.json').read_text())
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
        print(f"  GIF: {root / entry['gif']}\n  六帧图: {root / entry['filmstrip']}")
        if entry.get('related'):
            print('  相关: ' + ', '.join(entry['related']))
        print()


if __name__ == '__main__':
    main()
