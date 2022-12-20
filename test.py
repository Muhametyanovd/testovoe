import unittest
from main import encryptxor


class TestEnctryptxor(unittest.TestCase):
    def test_numeric(self):
        self.assertEqual(encryptxor('1234567890', '0987654321'), '')

    def test_russian(self):
        self.assertEqual(encryptxor('цмик', 'спк'), '')

    def test_english(self):
        self.assertEqual(encryptxor("onetwo", "three"), '')
