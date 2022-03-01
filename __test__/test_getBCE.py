import unittest

import pandas.core.frame

from getBCE.menu import *


def query():
    return getBCE('2020', 'enero', '050')


class MyTestCase(unittest.TestCase):

    def test_if_returns_string(self):
        self.assertIsInstance(query().href, str)

    def test_if_arguments_are_string(self):
        with self.assertRaises(Exception):
            self.assertRaises(Exception, getBCE())

    def test_if_table_begins_with_none(self):
        self.assertEqual(str(type(query().table)), "<class 'NoneType'>")

    def test_if_create_table_works(self):
        table = getBCE('2020', 'enero', '050')
        table.createTable()
        self.assertIsInstance(table.table, pandas.core.frame.DataFrame)


if __name__ == '__main__':
    unittest.main()
