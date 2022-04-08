import unittest
from getBCE.lector import *

main = "https://contenido.bce.fin.ec/home1/estadisticas/bolmensual/IEMensual.jsp"


class Reader(unittest.TestCase):

    reader = Reader(main, False)

    def test_reader_returns_dictionary(self):
        self.assertIsInstance(self.reader.result, dict)

    def test_if_result_contains_href_and_page(self):
        expected_keys = ['href', 'page']
        self.assertEqual(expected_keys, list(self.reader.result.keys()))

    def test_if_href_and_page_are_lists(self):
        self.assertIsInstance(self.reader.result['href'], list)
        self.assertIsInstance(self.reader.result['page'], list)


if __name__ == '__main__':
    unittest.main()
