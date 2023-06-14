import unittest
from main import is_palindrome


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(True, is_palindrome('wasitacaroracatisaw'))

    def test_2(self):
        self.assertEqual(False, is_palindrome('rishdararardeshir'))

    def test_3(self):
        self.assertEqual(True, is_palindrome(''))