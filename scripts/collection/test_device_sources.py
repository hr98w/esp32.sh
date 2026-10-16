import unittest
from unittest.mock import patch
from discover_devices import extract

HTML='''<h1>Example board</h1><p class="byline"><a href="/esp32/manufacturer/seeed-studio/">Seeed Studio</a></p><a href="/esp32/microcontroller/esp32s3/">ESP32-S3</a><p class="sub">Device summary</p><a href="https://files.example.com/chip.pdf">Datasheet</a><a href="https://maker.example.com/board?sku=12&amp;utm_source=directory&amp;sensecap_affiliate=abc">Buy on Store</a>'''
class DeviceSourceTests(unittest.TestCase):
 def test_device_documentation_override_beats_chip_pdf(self):
  with patch('discover_devices._read',return_value={'board':{'url':'https://wiki.example.com/actual-board/'}}):
   self.assertEqual(extract(HTML,'https://directory.example.com/esp32/board/')['officialUrl'],'https://wiki.example.com/actual-board/')
 def test_unassigned_brand_is_kept_unknown_instead_of_inferred_from_model_name(self):
  import re
  html=re.sub(r'<p class="byline">.*?</p>','',HTML)
  with patch('discover_devices._read',return_value={}):
   record=extract(html,'https://directory.example.com/esp32/board/')
   self.assertEqual(record['manufacturer']['id'],'unknown')
   self.assertTrue(record['manufacturerNeedsReview'])
 def test_device_wiki_is_preferred_to_ambiguous_chip_datasheet(self):
  with patch('discover_devices._read',return_value={}):
   record=extract(HTML+'<a href="https://wiki.maker.example.com/board">Official device wiki</a>','https://directory.example.com/esp32/board/')
   self.assertEqual(record['officialUrl'],'https://wiki.maker.example.com/board')
 def test_hookup_guide_beats_product_and_reseller_links(self):
  html=HTML.replace('<a href="https://files.example.com/chip.pdf">Datasheet</a>','')+'<a href="https://maker.example.com/product">SparkFun product page</a><a href="https://learn.maker.example.com/board">Board Hookup Guide</a>'
  with patch('discover_devices._read',return_value={}):
   self.assertEqual(extract(html,'https://directory.example.com/esp32/board/')['officialUrl'],'https://learn.maker.example.com/board')
 def test_tracking_is_removed_without_dropping_functional_variant_query(self):
  with patch('discover_devices._read',return_value={}):
   record=extract(HTML.replace('>Datasheet<','>File<'),'https://directory.example.com/esp32/board/')
   self.assertEqual(record['officialUrl'],'https://maker.example.com/board?sku=12')
if __name__=='__main__':unittest.main()
