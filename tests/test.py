# tests/test.py

import unittest
from adsb_exchange_api_nafeeur import AdsbExchangeAPI

class TestAdsbExchangeAPI(unittest.TestCase):
    def setUp(self):
        # Use a dummy API key for testing purposes
        self.api_key = 'DUMMY_API_KEY'
        self.api = AdsbExchangeAPI(api_key=self.api_key)

    def test_initialization(self):
        self.assertEqual(self.api.headers["x-rapidapi-key"], self.api_key)

if __name__ == '__main__':
    unittest.main()
