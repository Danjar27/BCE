import unittest
from getBCE.Main import Search, get_bce


class Main(unittest.TestCase):

    def test_if_search_select_returns_string(self):
        search: Search = Search()
        search.set_date('2021', 'enero', show=False)
        self.assertIsInstance(search.select('055'), str)

    def test_if_search_returns_same_as_get_bce(self):
        search: Search = Search()
        search.set_date('2021', 'enero', show=False)
        search_result = search.select('055')
        self.assertEqual(get_bce('2021', 'enero', '055'), search_result)


if __name__ == '__main__':
    unittest.main()
