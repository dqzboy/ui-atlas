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
    def check_media(label, key, value, expected, signatures, doc):
        if value != expected:
            errors.append(f'{label}: unexpected {key} path')
        path = (root / value).resolve()
        if not path.is_relative_to(root.resolve()):
            errors.append(f'{label}: {key} outside skill directory')
            return
        if not path.is_file():
            errors.append(f'{label}: missing {key}')
        else:
            with path.open('rb') as media:
                header = media.read(6)
            if not header.startswith(signatures):
                errors.append(f'{label}: invalid {key} header')
        if f'../{value}' not in doc:
            errors.append(f'{label}: missing {key} document link')

    required = ('id', 'category', 'category_title', 'slug', 'name', 'english',
                'summary', 'prompt', 'kind')
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
        media_type = entry.get('media_type', 'animation')
        if media_type == 'gallery':
            images = entry.get('images')
            if not isinstance(images, list) or not images:
                errors.append(f'{label}: gallery needs a nonempty images list')
            else:
                if len(set(images)) != len(images):
                    errors.append(f'{label}: duplicate gallery image')
                for number, value in enumerate(images, 1):
                    check_media(label, f'image {number}', value,
                                f'assets/images/{category}/{slug}-{number:02}.jpg',
                                (b'\xff\xd8\xff',), doc)
            if entry.get('preview'):
                check_media(label, 'preview', entry['preview'],
                            f'assets/previews/{category}/{slug}.jpg',
                            (b'\xff\xd8\xff',), doc)
            else:
                errors.append(f'{label}: missing gallery preview')
            if entry.get('gif') or entry.get('filmstrip'):
                errors.append(f'{label}: static gallery cannot declare animation media')
        elif media_type == 'animation':
            for key, folder, suffix, signatures in [
                ('gif', 'gifs', '.gif', (b'GIF87a', b'GIF89a')),
                ('filmstrip', 'filmstrips', '.jpg', (b'\xff\xd8\xff',)),
            ]:
                if not entry.get(key):
                    errors.append(f'{label}: missing {key}')
                    continue
                check_media(label, key, entry[key],
                            f'assets/{folder}/{category}/{slug}{suffix}',
                            signatures, doc)
        else:
            errors.append(f'{label}: unknown media_type {media_type}')
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
    galleries = sum(entry.get('media_type') == 'gallery' for entry in data['items'])
    images = sum(len(entry.get('images', [])) for entry in data['items'])
    print(f"Validated {len(data['items'])} entries in {len(data['categories'])} categories: "
          f"{counts['pattern']} patterns, {counts['rule']} rules; "
          f"{len(data['items']) - galleries} animations, {galleries} galleries / {images} images; "
          'all media and references exist.')


if __name__ == '__main__':
    main()
