import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from public_fetch import fetch_public, Deferred, validate_url

class PublicFetchTests(unittest.TestCase):
    def test_rejects_identity_in_url(self):
        for url in ['http://example.com', 'https://user:secret@github.com/a/b', 'https://api.github.com/a?access_token=x']:
            with self.assertRaises(ValueError): validate_url(url)
    def test_offline_never_connects(self):
        with tempfile.TemporaryDirectory() as temp, patch('public_fetch._curl') as network:
            with self.assertRaises(Deferred): fetch_public('https://example.com/data', offline=True, cache_dir=temp)
            network.assert_not_called()
    def test_cache_and_failure_preserve_last_success(self):
        with tempfile.TemporaryDirectory() as temp:
            url='https://example.com/data'
            with patch('public_fetch._curl', return_value=(200, {'etag':'v1'}, b'{"stars":12}')):
                first=fetch_public(url,cache_dir=temp)
            with patch('public_fetch._curl') as network:
                second=fetch_public(url,offline=True,cache_dir=temp)
                self.assertEqual(first['body'], second['body']);network.assert_not_called()
            with patch('public_fetch.time.sleep'), patch('public_fetch._curl',return_value=(429,{'retry-after':'120'},b'')):
                with self.assertRaises(Deferred): fetch_public(url,ttl=0,cache_dir=temp)
            with patch('public_fetch._curl') as network:
                with self.assertRaises(Deferred): fetch_public(url,ttl=0,cache_dir=temp)
                network.assert_not_called()
            self.assertEqual(fetch_public(url,offline=True,cache_dir=temp)['body'], b'{"stars":12}')
    def test_http_date_retry_after_and_zero_remaining_success(self):
        with tempfile.TemporaryDirectory() as temp, patch('public_fetch._curl',return_value=(429,{'retry-after':'Thu, 15 Oct 2099 18:00:00 GMT'},b'')):
            with self.assertRaises(Deferred):fetch_public('https://example.com/data',cache_dir=temp)
            with patch('public_fetch._curl') as network:
                with self.assertRaises(Deferred):fetch_public('https://example.com/other',cache_dir=temp)
                network.assert_not_called()
        with tempfile.TemporaryDirectory() as temp, patch('public_fetch._curl',return_value=(200,{'x-ratelimit-remaining':'0','x-ratelimit-reset':'4102444800'},b'last allowed response')):
            self.assertEqual(fetch_public('https://example.com/data',cache_dir=temp)['body'],b'last allowed response')
            with patch('public_fetch._curl') as network:
                with self.assertRaises(Deferred):fetch_public('https://example.com/other',cache_dir=temp)
                network.assert_not_called()
    def test_conditional_revalidation(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch('public_fetch._curl',return_value=(200,{'etag':'v1'},b'old')): fetch_public('https://example.com/data',cache_dir=temp)
            with patch('public_fetch.time.sleep'),patch('public_fetch._curl',return_value=(304,{},b'')) as network:
                result=fetch_public('https://example.com/data',ttl=0,cache_dir=temp)
                self.assertEqual(result['body'],b'old')
                self.assertEqual(network.call_args.args[1]['If-None-Match'],'v1')

if __name__=='__main__': unittest.main()
