#!/usr/bin/env python3
"""Validate UI Atlas catalog IDs, references and bundled media paths."""
import json
from collections import Counter
from pathlib import Path
import sys


def validate(root):
    data = json.loads((root / 'references/catalog.json').read_text())
    errors = []
    category_ids = [category['id'] for category in data['categories']]
    ids = [entry['id'] for entry in data['items']]
    for label, values in [('category', category_ids), ('entry', ids)]:
        errors.extend(f'Duplicate {label}: {key}' for key, count in
                      Counter(values).items() if count > 1)
    categories = {category['id']: category['title']
                  for category in data['categories']}
    known_ids = set(ids)
    docs = {}
    for category in categories:
        path = root / 'references' / f'{category}.md'
        if path.is_file():
            docs[category] = path.read_text()
        else:
            errors.append(f'Missing category document: {path}')
    required = ('id', 'category', 'category_title', 'slug', 'name', 'english',
                'summary', 'prompt', 'kind', 'gif', 'filmstrip')
    for entry in data['items']:
        label = entry.get('id', '<missing ID>')
        missing = [key for key in required if not entry.get(key)]
        if missing:
            errors.append(f'{label}: missing {missing}')
            continue
        category, slug = entry['category'], entry['slug']
        if category not in categories:
            errors.append(f'{label}: unknown category {category}')
        if categories.get(category) != entry['category_title']:
            errors.append(f'{label}: category title mismatch')
        if label != f'{category}/{slug}':
            errors.append(f'{label}: category/slug mismatch')
        if entry['kind'] not in {'pattern', 'rule'}:
            errors.append(f'{label}: unknown kind {entry["kind"]}')
        doc = docs.get(category, '')
        if f'<a id="{slug}"></a>' not in doc:
            errors.append(f'{label}: missing document anchor')
        if f'`{label}`' not in doc:
            errors.append(f'{label}: missing document entry')
        for key, folder, suffix, signatures in [
            ('gif', 'gifs', '.gif', (b'GIF87a', b'GIF89a')),
            ('filmstrip', 'filmstrips', '.jpg', (b'\xff\xd8\xff',)),
        ]:
            expected = f'assets/{folder}/{category}/{slug}{suffix}'
            if entry[key] != expected:
                errors.append(f'{label}: unexpected {key} path')
            path = (root / entry[key]).resolve()
            if not path.is_relative_to(root.resolve()):
                errors.append(f'{label}: {key} outside skill directory')
                continue
            if not path.is_file():
                errors.append(f'{label}: missing {key}')
            else:
                with path.open('rb') as media:
                    header = media.read(6)
                if not header.startswith(signatures):
                    errors.append(f'{label}: invalid {key} header')
            if f'../{entry[key]}' not in doc:
                errors.append(f'{label}: missing {key} document link')
        for related in entry.get('related', []):
            if related not in known_ids:
                errors.append(f'{label}: unknown related entry {related}')
    return data, errors


def main():
    root = Path(__file__).resolve().parent.parent
    try:
        data, errors = validate(root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Invalid library: {error}', file=sys.stderr)
        raise SystemExit(1)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    counts = Counter(entry['kind'] for entry in data['items'])
    print(f"Validated {len(data['items'])} entries in {len(data['categories'])} categories: "
          f"{counts['pattern']} patterns, {counts['rule']} rules; all media and references exist.")


if __name__ == '__main__':
    main()
