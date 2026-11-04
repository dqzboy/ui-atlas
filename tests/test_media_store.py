"""Exercise offline install, cache reuse, failed downloads, and manifest integrity."""
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import media_store
from validate_library import validate


class MediaStoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'installed-skill'
        self.root.mkdir()
        self.env = patch.dict(os.environ, {'UI_ATLAS_CACHE_DIR': str(Path(self.tmp.name) / 'cache')})
        self.env.start()
        self.addCleanup(self.env.stop)
        self.value = 'assets/filmstrips/motion/example.jpg'
        self.payload = b'\xff\xd8\xffexample-media'
        self.manifest = {'revision': 'a' * 40, 'base_url': 'https://example.test/revision',
                         'files': {self.value: {'bytes': len(self.payload),
                         'sha256': hashlib.sha256(self.payload).hexdigest()}}}

    def test_download_is_verified_and_reused_without_network(self):
        with patch('urllib.request.urlopen', return_value=io.BytesIO(self.payload)) as request:
            path = media_store.fetch(self.manifest, self.value, self.root)
        self.assertEqual(path.read_bytes(), self.payload)
        self.assertFalse(path.is_relative_to(self.root))
        request.assert_called_once()
        with patch('urllib.request.urlopen', side_effect=AssertionError('cache hit used network')):
            self.assertEqual(media_store.fetch(self.manifest, self.value, self.root), path)

    def test_corrupt_cache_is_replaced(self):
        path = media_store.cache_root(self.manifest) / self.value
        path.parent.mkdir(parents=True)
        path.write_bytes(b'corrupt')
        with patch('urllib.request.urlopen', return_value=io.BytesIO(self.payload)):
            self.assertEqual(media_store.fetch(self.manifest, self.value, self.root).read_bytes(), self.payload)

    def test_wrong_download_hash_never_becomes_a_cache_hit(self):
        with patch('urllib.request.urlopen', return_value=io.BytesIO(b'x' * len(self.payload))):
            with self.assertRaisesRegex(ValueError, 'checksum'):
                media_store.fetch(self.manifest, self.value, self.root)
        self.assertIsNone(media_store.local_media(self.manifest, self.value, self.root))
        self.assertFalse(list(Path(self.tmp.name).rglob('.download-*')))

    def test_network_failure_does_not_leave_partial_media(self):
        with patch('urllib.request.urlopen', side_effect=urllib.error.URLError('offline')):
            with self.assertRaises(urllib.error.URLError):
                media_store.fetch(self.manifest, self.value, self.root)
        self.assertFalse(list(Path(self.tmp.name).rglob('.download-*')))

    def test_path_cannot_escape_media_cache(self):
        for value in ('../outside.jpg', '/tmp/outside.jpg', 'assets/../../outside.jpg', 'scripts/a.py'):
            with self.assertRaises(ValueError):
                media_store.media_url(self.manifest, value)

    def test_selection_avoids_unrequested_media(self):
        animation = {'media_type': 'animation', 'filmstrip': 'a.jpg', 'gif': 'a.gif'}
        filmstrip = {'media_type': 'filmstrip', 'filmstrip': 'a.jpg'}
        gallery = {'media_type': 'gallery', 'preview': 'p.jpg', 'images': ['1.jpg', '2.jpg']}
        self.assertEqual(media_store.entry_media(filmstrip), ['a.jpg'])
        self.assertEqual(media_store.entry_media(filmstrip, 'all'), ['a.jpg'])
        self.assertEqual(media_store.entry_media(animation), ['a.jpg'])
        self.assertEqual(media_store.entry_media(animation, 'images'), ['a.jpg'])
        self.assertEqual(media_store.entry_media(animation, 'gif'), ['a.gif'])
        self.assertEqual(media_store.entry_media(animation, 'all'), ['a.jpg', 'a.gif'])
        with self.assertRaisesRegex(ValueError, '没有 GIF'):
            media_store.entry_media(filmstrip, 'gif')
        with self.assertRaises(ValueError):
            media_store.entry_media(gallery, 'gif')
        self.assertEqual(media_store.entry_media(gallery), ['p.jpg'])
        self.assertEqual(media_store.entry_media(gallery, 'images'), ['1.jpg', '2.jpg'])
        self.assertEqual(media_store.entry_media({'media_type': 'recipe'}), [])

    def test_core_library_validates_with_no_cache_and_no_network(self):
        with patch('urllib.request.urlopen', side_effect=AssertionError('validation used network')):
            data, errors = validate(media_store.ROOT)
        self.assertFalse(errors, errors)
        self.assertEqual(sum(e.get('media_type') == 'recipe' for e in data['items']), 10)
        manifest = media_store.load_manifest()
        # All default previews stay lightweight, including references retaining a GIF.
        previews = [p for e in data['items'] for p in media_store.entry_media(e)]
        self.assertTrue(all(Path(p).suffix == '.jpg' for p in previews))
        self.assertEqual({p for p in manifest['files'] if p.endswith('.gif')},
                         {e['gif'] for e in data['items'] if e['media_type'] == 'animation'})
        paths = [p for e in data['items'] for p in media_store.entry_media(e, 'all')]
        self.assertEqual(set(paths), set(manifest['files']))


if __name__ == '__main__':
    unittest.main()
