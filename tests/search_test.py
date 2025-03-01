import unittest

from gemasearch.data import Werk
from gemasearch.search import GemaMusicSearch


class TestGemaMusicSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = GemaMusicSearch()

    def test_search_bohemian_rhapsody(self):
        result = self.searcher.search("Bohemian Rhapsody")

        self.assertIsInstance(result, list, "Response should be a list.")
        self.assertGreater(len(result), 0, "Response should at least contain one entry.")

        first_entry = result[0]

        self.assertIsInstance(first_entry, Werk, "Track entry should be of type Werk.")


if __name__ == "__main__":
    unittest.main()
