import unittest
from my_awesome_lib.text_processing import count_words, reverse_text, remove_punctuation

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")
        self.assertEqual(reverse_text(""), "")

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")
        self.assertEqual(remove_punctuation(""), "")

if __name__ == "__main__":
    unittest.main()
