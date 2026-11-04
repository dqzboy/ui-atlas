"""Keep complete reference documents and lightweight release documents usable."""
import re

from media_store import media_url


DETAIL_BLOCK = re.compile(
    r'<!-- ui-atlas:details ([^\s]+) -->\n.*?<!-- /ui-atlas:details -->', re.S)


def lightweight_document(text, entries, manifest, quality):
    by_id = {entry['id']: entry for entry in entries}

    def preview(match):
        entry = by_id[match[1]]
        if entry['media_type'] == 'recipe':
            return ''
        value = entry.get('filmstrip') or entry['preview']
        return f"![{entry['name']}：轻量总览]({media_url(manifest, value)})"

    text = DETAIL_BLOCK.sub(preview, text)
    # Recipe documents use full-size GIFs in the complete edition, and declared
    # bundled clips in the lightweight edition. No unpublished remote URL is made.
    for entry in entries:
        detail = quality['entries'].get(entry['id'], {})
        if entry['media_type'] == 'recipe' and detail.get('gif'):
            text = text.replace('../../' + detail['gif'], '../../' + entry['gif'])

    def remote(match):
        value = match['value']
        record = manifest['files'].get(value)
        if record and not record.get('bundled'):
            return '](' + media_url(manifest, value) + ')'
        return match[0]

    return re.sub(r'\]\((?:\.\./){1,2}(?P<value>assets/[^)]+)\)', remote, text)
