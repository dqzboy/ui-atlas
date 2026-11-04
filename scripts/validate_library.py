#!/usr/bin/env python3
"""Validate UI Atlas catalog, recipes and selectively retained reference media."""
import argparse
import re
import json
from collections import Counter
from pathlib import Path
import sys

from media_store import checked_path, load_manifest, local_media, media_url
from detail_media import validate_quality


def validate(root, check_media=False):
    data = json.loads((root / 'references/catalog.json').read_text())
    manifest = load_manifest(root)
    errors = []
    used_media = set()
    revision = manifest.get('revision', '')
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        errors.append('Media revision must be an immutable Git commit')
    if manifest.get('base_url') != 'https://raw.githubusercontent.com/dqzboy/ui-atlas/' + revision:
        errors.append('Unexpected media origin or revision')
    for value in manifest['files']:
        if Path(value).suffix not in {'.jpg', '.png', '.webp'} and not (
                value.startswith('assets/recipes/') and value.endswith('.gif')
                and manifest['files'][value].get('bundled')):
            errors.append(f'Unsupported reference format: {value}')
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
    def check_asset(label, key, value, expected, signatures, doc):
        if value != expected:
            errors.append(f'{label}: unexpected {key} path')
        try:
            checked_path(value)
            record = manifest['files'][value]
        except (ValueError, KeyError):
            errors.append(f'{label}: missing or invalid media record {value}')
            return
        used_media.add(value)
        if (not isinstance(record.get('bytes'), int) or record['bytes'] <= 0
                or not re.fullmatch(r'[0-9a-f]{64}', record.get('sha256', ''))):
            errors.append(f'{label}: invalid media size/hash {value}')
        bundled = record.get('bundled', False)
        if bundled and not value.startswith(('assets/recipes/', 'assets/details/')):
            errors.append(f'{label}: bundled media must be a declared reference visual')
        links = ['../' + value]
        if not bundled:
            links.append(media_url(manifest, value))
        if not any(link in doc for link in links):
            errors.append(f'{label}: missing {key} document link')
        if check_media or bundled:
            path = local_media(manifest, value, root)
            if not path:
                recovery = ('reinstall the skill' if bundled else 'run fetch_media.py --all')
                errors.append(f'{label}: uncached or corrupt {value}; {recovery}')
            else:
                with path.open('rb') as media:
                    header = media.read(6)
                if not header.startswith(signatures):
                    errors.append(f'{label}: invalid {key} header')

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
        media_type = entry.get('media_type')
        if not entry.get('media_reason'):
            errors.append(f'{label}: missing per-entry media decision reason')
        if media_type == 'recipe':
            expected = f'references/recipes/{slug}.md'
            if entry.get('recipe') != expected or not (root / expected).is_file():
                errors.append(f'{label}: missing or unexpected recipe')
            elif f'recipes/{slug}.md' not in doc:
                errors.append(f'{label}: missing recipe document link')
            else:
                recipe = (root / expected).read_text()
                if re.search(r'https?://|Kubai087|枯白|关注我', recipe, re.I):
                    errors.append(f'{label}: source identity or external link in recipe')
            if entry.get('evidence') != 'implementation-recipe':
                errors.append(f'{label}: recipe evidence type missing')
            expected_visual = ('sampled-demo-frames-and-clip' if entry.get('gif')
                               else 'sampled-demo-frames')
            if entry.get('visual_evidence') != expected_visual:
                errors.append(f'{label}: missing or incorrect recipe visual evidence')
            for key in ('preview', 'gif'):
                value = entry.get(key)
                if key == 'preview' and not value:
                    errors.append(f'{label}: missing recipe preview')
                if not value:
                    continue
                suffix = '.jpg' if key == 'preview' else '.gif'
                check_asset(label, key, value, f'assets/recipes/{slug}{suffix}',
                            (b'\xff\xd8\xff',) if key == 'preview' else (b'GIF87a', b'GIF89a'), doc)
                if not manifest['files'].get(value, {}).get('bundled'):
                    errors.append(f'{label}: recipe visual must be bundled')
                if (root / expected).is_file() and '../../' + value not in (root / expected).read_text():
                    errors.append(f'{label}: missing recipe visual link')
            if entry.get('filmstrip') or entry.get('images'):
                errors.append(f'{label}: unexpected recipe visual fields')
        elif media_type in {'image', 'gallery'}:
            images = entry.get('images')
            if not isinstance(images, list) or not images:
                errors.append(f'{label}: gallery needs a nonempty images list')
            else:
                if len(set(images)) != len(images):
                    errors.append(f'{label}: duplicate gallery image')
                for number, value in enumerate(images, 1):
                    if not value.startswith(f'assets/details/{category}/') or Path(value).suffix not in {'.png', '.webp'}:
                        errors.append(f'{label}: invalid selected image path')
                    check_asset(label, f'image {number}', value, value,
                                (b'RIFF',) if value.endswith('.webp') else (b'\x89PNG\r\n',), doc)
            if entry.get('preview'):
                if entry['preview'] not in (images or []):
                    errors.append(f'{label}: preview must be one of the selected images')
                check_asset(label, 'preview', entry['preview'], entry['preview'],
                            (b'RIFF',) if entry['preview'].endswith('.webp') else (b'\x89PNG\r\n',), doc)
            else:
                errors.append(f'{label}: missing gallery preview')
            if entry.get('gif') or entry.get('filmstrip'):
                errors.append(f'{label}: static gallery cannot declare animation media')
        elif media_type in {'animation', 'filmstrip'}:
            expected_evidence = ('animated-reference' if media_type == 'animation'
                                 else 'sampled-animation-frames')
            if entry.get('evidence') != expected_evidence:
                errors.append(f'{label}: missing or incorrect media evidence type')
            if media_type == 'animation':
                if not entry.get('gif'):
                    errors.append(f'{label}: animation needs a GIF')
                else:
                    check_asset(label, 'gif', entry['gif'],
                                f'assets/gifs/{category}/{slug}.gif',
                                (b'GIF87a', b'GIF89a'), doc)
            elif 'gif' in entry:
                errors.append(f'{label}: image-only entry cannot declare a GIF')
            if not entry.get('filmstrip'):
                errors.append(f'{label}: missing filmstrip')
            else:
                check_asset(label, 'filmstrip', entry['filmstrip'],
                            f'assets/filmstrips/{category}/{slug}.jpg',
                            (b'\xff\xd8\xff',), doc)

        else:
            errors.append(f'{label}: unknown media_type {media_type}')
        for related in entry.get('related', []):
            if related not in known_ids:
                errors.append(f'{label}: unknown related entry {related}')
    for value in set(manifest['files']) - used_media:
        errors.append(f'Unreferenced media record: {value}')
    errors.extend(validate_quality(root))
    # Validate Markdown file links and explicit catalog anchors, outside code fences.
    for path in [root / 'SKILL.md', root / 'README.md', *(root / 'references').rglob('*.md')]:
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith('#'):
                continue
            file, _, anchor = target.partition('#')
            destination = (path.parent / file).resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.is_file():
                errors.append(f'{path.name}: broken local link {target}')
            elif anchor and destination.parent == root / 'references' and destination.name not in {'index.md', 'craft-recipes.md'}:
                if f'<a id="{anchor}"></a>' not in destination.read_text():
                    errors.append(f'{path.name}: broken anchor {target}')
    return data, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-media', action='store_true', help='校验完整离线缓存的文件头、大小和 SHA-256')
    parser.add_argument('--check-quality', action='store_true', help='额外校验可选原尺寸细节库')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    try:
        data, errors = validate(root, args.check_media)
        if args.check_quality:
            errors.extend(validate_quality(root, check_files=True))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Invalid library: {error}', file=sys.stderr)
        raise SystemExit(1)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    kinds = Counter(e.get('media_type') for e in data['items'])
    print(f"Validated {len(data['items'])} entries / {len(data['categories'])} categories: "
          f"{kinds['image']} image references, {kinds['animation']} animations, "
          f"{kinds['gallery']} galleries, {kinds['recipe']} recipes; "
          + ('offline cache verified.' if args.check_media else 'manifest and links valid (no download).'))


if __name__ == '__main__':
    main()
