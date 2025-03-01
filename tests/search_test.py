import unittest

from gemasearch.search import GemaMusicSearch


class TestGemaMusicSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = GemaMusicSearch()

    def test_search_bohemian_rhapsody(self):
        result = self.searcher.search("wolkeplatz")

        for title in result.get('titel', []):
            print(title)

        self.assertIsInstance(result, dict, "Response should be a dictionary")
        self.assertIn("titel", result, "Response should contain 'items'")


if __name__ == "__main__":
    unittest.main()
