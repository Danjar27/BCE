import unittest
from getBCE.utils import *


class Utils(unittest.TestCase):

    def test_if_destructuring_works(self):
        user = {"name": "test", "age": 15}
        name, age = destructure(user)
        self.assertIsInstance(name, str)
        self.assertIsInstance(age, int)

    def test_if_boundaries_works(self):
        array = [1, 2, 3, 4, 5]
        array = set_bounders(array, 3)
        self.assertEqual(len(array), 2)

    def test_if_index_is_created(self):
        array = [1, 2, 3, 4, 5]
        index = create_index_for_list(array)
        self.assertEqual(len(index), len(array))
        self.assertIsInstance(index[3], str)


if __name__ == '__main__':
    unittest.main()
