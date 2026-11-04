"""Exercise offline install, cache reuse, failed downloads, and manifest integrity."""
import hashlib
import io
import json
import os
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import media_store
from validate_library import validate
from detail_media import detail_paths, detail_values, validate_quality, image_dimensions
from fetch_media import selected_media
from reference_docs import lightweight_document


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
        recipe = {'media_type': 'recipe', 'preview': 'p.jpg', 'gif': 'clip.gif'}
        self.assertEqual(media_store.entry_media(recipe), ['p.jpg'])
        self.assertEqual(media_store.entry_media(recipe, 'all'), ['p.jpg', 'clip.gif'])
        self.assertEqual(media_store.entry_media(recipe, 'gif'), ['clip.gif'])
        with self.assertRaisesRegex(ValueError, '没有 GIF'):
            media_store.entry_media({'media_type': 'recipe', 'preview': 'p.jpg'}, 'gif')

    def test_bundled_media_never_uses_remote_origin_or_cache(self):
        record = self.manifest['files'][self.value]
        record['bundled'] = True
        cached = media_store.cache_root(self.manifest) / self.value
        cached.parent.mkdir(parents=True)
        cached.write_bytes(self.payload)
        with patch('urllib.request.urlopen', side_effect=AssertionError('bundled media used network')):
            with self.assertRaises(FileNotFoundError):
                media_store.fetch(self.manifest, self.value, self.root)
            local = self.root / self.value
            local.parent.mkdir(parents=True)
            local.write_bytes(self.payload)
            self.assertEqual(media_store.fetch(self.manifest, self.value, self.root), local)
            local.write_bytes(b'corrupt')
            with self.assertRaises(FileNotFoundError):
                media_store.fetch(self.manifest, self.value, self.root)
        with self.assertRaisesRegex(ValueError, 'no remote URL'):
            media_store.media_url(self.manifest, self.value)

    def test_core_library_validates_with_no_cache_and_no_network(self):
        with patch('urllib.request.urlopen', side_effect=AssertionError('validation used network')):
            data, errors = validate(media_store.ROOT)
        self.assertFalse(errors, errors)
        self.assertEqual(sum(e.get('media_type') == 'recipe' for e in data['items']), 10)
        manifest = media_store.load_manifest()
        # All default previews stay lightweight, including references retaining a GIF.
        previews = [p for e in data['items'] for p in media_store.entry_media(e)]
        self.assertTrue(all(Path(p).suffix in {'.jpg', '.png', '.webp'} for p in previews))
        self.assertEqual({p for p in manifest['files'] if p.endswith('.gif')},
                         {e['gif'] for e in data['items'] if e.get('gif')})
        paths = [p for e in data['items'] for p in media_store.entry_media(e, 'all')]
        self.assertEqual(set(paths), set(manifest['files']))

    def test_release_contains_working_recipe_visuals_without_cache(self):
        subprocess.run([sys.executable, str(media_store.ROOT / 'scripts/build_skill.py')],
                       check=True, capture_output=True)
        with zipfile.ZipFile(media_store.ROOT / 'dist/ui-atlas.zip') as archive:
            archive.extractall(self.root)
        installed = self.root / 'ui-atlas'
        manifest = media_store.load_manifest(installed)
        data, errors = validate(installed)
        self.assertFalse(errors, errors)
        recipes = [e for e in data['items'] if e['media_type'] == 'recipe']
        self.assertEqual(len(recipes), 10)
        self.assertEqual(sum(bool(e.get('gif')) for e in recipes), 5)
        self.assertTrue(all(not e.get('gif') for e in data['items'] if e['media_type'] != 'recipe'))
        with patch('urllib.request.urlopen', side_effect=AssertionError('offline recipe used network')):
            for entry in recipes:
                for value in media_store.entry_media(entry, 'all'):
                    self.assertEqual(media_store.fetch(manifest, value, installed), installed / value)
        bundled = {p for p, r in manifest['files'].items() if r.get('bundled')}
        self.assertEqual({p.relative_to(installed).as_posix()
                          for p in (installed / 'assets').rglob('*') if p.is_file()}, bundled)

    def test_detail_selection_requires_every_image_to_be_verified(self):
        first = 'assets/details/motion/example-01.png'
        second = 'assets/details/motion/example-02.png'
        record = {'bytes': len(self.payload), 'sha256': hashlib.sha256(self.payload).hexdigest()}
        quality = {'revision': 'b' * 40, 'entries': {'motion/example': {'images': [first, second]}},
                   'files': {first: record, second: record}}
        for value in (first, second):
            path = self.root / value
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(self.payload)
        self.assertEqual(detail_paths('motion/example', 'images', self.root, quality),
                         [self.root / first, self.root / second])
        (self.root / second).write_bytes(b'corrupt')
        self.assertEqual(detail_paths('motion/example', 'images', self.root, quality), [])
        self.assertEqual(detail_paths('motion/example', 'gif', self.root, quality), [])
        self.assertEqual(detail_paths('motion/example', 'preview', self.root, quality), [])

    def test_optional_details_do_not_require_network_or_installation(self):
        with patch('urllib.request.urlopen', side_effect=AssertionError('details used network')):
            self.assertEqual(detail_paths('motion/example', 'images', self.root), [])
            self.assertEqual(validate_quality(media_store.ROOT), [])
            # Unpublished native screenshots are bundled; remote page images stay optional.
            subprocess.run([sys.executable, str(media_store.ROOT / 'scripts/build_skill.py')],
                           check=True, capture_output=True)
            with zipfile.ZipFile(media_store.ROOT / 'dist/ui-atlas.zip') as archive:
                self.assertIn('ui-atlas/references/media-quality.json', archive.namelist())
                manifest = media_store.load_manifest()
                actual = {name.removeprefix('ui-atlas/') for name in archive.namelist()
                          if '/assets/details/' in name}
                expected = {p for p, r in manifest['files'].items()
                            if p.startswith('assets/details/') and r.get('bundled')}
                self.assertEqual(actual, expected)

    def test_details_reject_paths_outside_detail_directory(self):
        for value in ('assets/../../outside.png', 'assets/recipes/example.png', '/tmp/example.png'):
            quality = {'entries': {'motion/example': {'images': [value]}}, 'files': {value: {}}}
            with self.assertRaises(ValueError):
                detail_paths('motion/example', 'images', self.root, quality)

    def test_documents_attach_every_selected_independent_image(self):
        self.assertFalse(validate_quality(media_store.ROOT))
        quality = json.loads((media_store.ROOT / 'references/media-quality.json').read_text())
        catalog = json.loads((media_store.ROOT / 'references/catalog.json').read_text())
        self.assertEqual(set(quality['entries']),
                         {e['id'] for e in catalog['items'] if e['media_type'] != 'recipe'})
        for entry_id, entry in quality['entries'].items():
            if entry.get('poster'):
                self.assertEqual(detail_values(entry_id, 'preview', quality), [entry['poster']])

    def test_lightweight_docs_keep_references_without_missing_detail_links(self):
        catalog = json.loads((media_store.ROOT / 'references/catalog.json').read_text())
        quality = json.loads((media_store.ROOT / 'references/media-quality.json').read_text())
        manifest = media_store.load_manifest()
        document = (media_store.ROOT / 'references/overlays.md').read_text()
        rendered = lightweight_document(document, catalog['items'], manifest, quality)
        poster = quality['entries']['overlays/drawer']['poster']
        self.assertIn('](../' + poster + ')', rendered)
        self.assertNotIn('assets/filmstrips/', rendered)
        self.assertIn('](../assets/recipes/overlay-decision.gif)', rendered)
        recipe = (media_store.ROOT / 'references/recipes/wiki-layout.md').read_text()
        rendered = lightweight_document(recipe, catalog['items'], manifest, quality)
        self.assertIn('](../../assets/recipes/wiki-layout.gif)', rendered)
        self.assertIn('](../../assets/recipes/wiki-layout.jpg)', rendered)

    def test_representative_images_avoid_temporal_duplicates(self):
        quality = json.loads((media_store.ROOT / 'references/media-quality.json').read_text())
        for entry_id in ('backgrounds/aurora', 'backgrounds/beams'):
            entry = quality['entries'][entry_id]
            self.assertEqual(entry['images'], [entry['poster']])
            self.assertEqual(detail_values(entry_id, 'images', quality),
                             detail_values(entry_id, 'preview', quality))
        # Distinct states and different pages still have their own references.
        self.assertEqual(len(quality['entries']['loading-errors/loading-button']['images']), 3)
        self.assertEqual(len(quality['entries']['mobile-workbenches/sales-crm-parcel-homes']['images']), 4)

    def test_quality_validation_detects_leftover_media_on_disk(self):
        references = self.root / 'references'
        references.mkdir()
        (references / 'catalog.json').write_text(json.dumps({'items': []}))
        (references / 'media-manifest.json').write_text(json.dumps({'revision': 'a' * 40}))
        (references / 'media-quality.json').write_text(json.dumps(
            {'base_revision': 'a' * 40, 'revision': 'b' * 40,
             'base_url': 'https://raw.githubusercontent.com/dqzboy/ui-atlas/' + 'b' * 40,
             'entries': {}, 'files': {}}))
        leftover = self.root / 'assets/details/leftover.png'
        leftover.parent.mkdir(parents=True)
        leftover.write_bytes(self.payload)
        self.assertEqual(validate_quality(self.root, check_files=True, check_links=False),
                         ['Unlisted detail file: assets/details/leftover.png'])

    def test_native_preview_downloads_on_demand_and_reuses_external_cache(self):
        value = 'assets/details/backgrounds/example.png'
        quality = {'revision': 'b' * 40, 'base_url': 'https://example.test/native-revision',
                   'entries': {'backgrounds/example': {'images': [value], 'poster': value}},
                   'files': {value: self.manifest['files'][self.value]}}
        entry = {'id': 'backgrounds/example', 'media_type': 'filmstrip', 'filmstrip': self.value}
        selection = selected_media(entry, 'preview', self.manifest, quality)
        self.assertEqual(selection, [(quality, value)])
        self.assertEqual(detail_paths(entry['id'], 'preview', self.root, quality), [])
        with patch('urllib.request.urlopen', return_value=io.BytesIO(self.payload)) as request:
            path = media_store.fetch(*selection[0], self.root)
        request.assert_called_once()
        self.assertFalse(path.is_relative_to(self.root))
        with patch('urllib.request.urlopen', side_effect=AssertionError('cache hit used network')):
            self.assertEqual(media_store.fetch(quality, value, self.root), path)
            self.assertEqual(detail_paths(entry['id'], 'preview', self.root, quality), [path])

    def test_current_library_is_static_and_only_selected_panels_remain(self):
        catalog = json.loads((media_store.ROOT / 'references/catalog.json').read_text())
        quality = json.loads((media_store.ROOT / 'references/media-quality.json').read_text())
        self.assertEqual(sum(e['media_type'] == 'gallery' for e in catalog['items']), 12)
        self.assertTrue(all(not e.get('gif') and e['media_type'] != 'animation'
                            for e in catalog['items'] if e['media_type'] != 'recipe'))
        self.assertTrue(all(Path(value).suffix in {'.png', '.webp'} for value in quality['files']))
        self.assertNotIn('enterprise-workbenches/blue-welcome-operations-portal',
                         {e['id'] for e in catalog['items']})

    def test_all_selection_deduplicates_preview_and_detail_records(self):
        value = 'assets/details/motion/example.png'
        entry = {'id': 'motion/example', 'media_type': 'image', 'preview': value,
                 'images': [value]}
        quality = {'entries': {'motion/example': {'poster': value, 'images': [value]}}}
        self.assertEqual(media_store.entry_media(entry, 'all'), [value])
        self.assertEqual(selected_media(entry, 'all', self.manifest, quality), [(quality, value)])

    def test_bundled_webp_dimensions_match_the_actual_file_header(self):
        quality = json.loads((media_store.ROOT / 'references/media-quality.json').read_text())
        for value, record in quality['files'].items():
            if value.endswith('.webp') and record.get('bundled'):
                with (media_store.ROOT / value).open('rb') as media:
                    dimensions = image_dimensions(media.read(32))
                self.assertEqual(dimensions, (record['width'], record['height']))
        with self.assertRaises(ValueError):
            image_dimensions(b'RIFFinvalid image')


if __name__ == '__main__':
    unittest.main()
