import unittest
from enrich_devices import extract
from verify_device_images import image_format

class DeviceEnrichmentTests(unittest.TestCase):
    def test_optional_closing_tags_keep_shared_guide_variants_in_separate_columns(self):
        # Seeed's shared guide omits </td> and </tr>; Plus memory must not become base memory.
        page='<table><tr><th>Product<th>XIAO S3<th>XIAO S3 Plus<tr><td>Flash<td>8MB<td>16MB</table>'
        tables=extract(page,'https://wiki.example.com/guide/')['tables']
        self.assertEqual(tables,[[['Product','XIAO S3','XIAO S3 Plus'],['Flash','8MB','16MB']]])
    def test_embedded_images_are_not_external_image_candidates(self):
        page='<img src="data:image/png;base64,AAAA"><img src="/photo.webp"><img src="/logo.svg">'
        images=extract(page,'https://maker.example.com/device/')['images']
        self.assertEqual([i['url'] for i in images],['https://maker.example.com/photo.webp'])
    def test_successful_html_response_is_not_a_verified_product_photo(self):
        self.assertIsNone(image_format(b'<!doctype html><h1>Product moved</h1>'))
        self.assertEqual(image_format(b'RIFFxxxxWEBPxxx'),'webp')
        # A .webp URL can return JPEG bytes; report the actual format.
        self.assertEqual(image_format(b'\xff\xd8\xff\xe0rest'),'jpeg')

if __name__=='__main__':unittest.main()
