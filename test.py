import unittest
from main import foo


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(foo('4', '1 2 1 2'), 1)

    def test_2(self):
        self.assertEqual(foo('5', '1 4 0 -1 3'), 1)

    def test_3(self):
        self.assertEqual(foo('6', '1 0 1 0 1 0'), 3)

    def test_4(self):
        self.assertEqual(foo('3', '1 7 1'), 1)

    def test_5(self):
        self.assertEqual(foo('4', '1 3 1 3'), 1)


if __name__ == '__main__':
    unittest.main()

