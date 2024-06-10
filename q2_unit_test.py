import unittest
from q2 import f

class TestCharacterCount(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(f(""), {})
    
    def test_single_character(self):
        self.assertEqual(f("a"), {'a': 1})
    
    def test_repeated_character(self):
        self.assertEqual(f("aaa"), {'a': 3})
    
    def test_multiple_characters(self):
        self.assertEqual(f("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
    
    def test_mixed_characters(self):
        self.assertEqual(f("abcabc"), {'a': 2, 'b': 2, 'c': 2})
    
    def test_spaces(self):
        self.assertEqual(f("a b c"), {'a': 1, ' ': 2, 'b': 1, 'c': 1})

if __name__ == '__main__':
    unittest.main()
