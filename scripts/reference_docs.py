"""Keep complete reference documents and lightweight release documents usable."""
import re

from media_store import media_url


DETAIL_BLOCK = re.compile(
    r'<!-- ui-atlas:details ([^\s]+) -->\n.*?<!-- /ui-atlas:details -->', re.S)


def lightweight_document(text, entries, manifest, quality):
    """Keep every native reference visible without bundling large media."""
    def remote(match):
        value = match['value']
        source = quality if value in quality['files'] else manifest
        record = source['files'].get(value)
        if record and not record.get('bundled'):
            return '](' + media_url(source, value) + ')'
        return match[0]

    return re.sub(r'\]\((?:\.\./){1,2}(?P<value>assets/[^)]+)\)', remote, text)


def offline_document(text, manifest, quality, prefix='../'):
    """Point fixed-version media links to files in the complete offline ZIP."""
    for source in (manifest, quality):
        text = text.replace(source['base_url'].rstrip('/') + '/assets/', prefix + 'assets/')
    return text
