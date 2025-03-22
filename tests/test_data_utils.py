import unittest
from my_awesome_lib.data_utils import parse_csv, save_to_csv
import os

class TestDataUtils(unittest.TestCase):
    def test_parse_csv(self):
        data = "name,age\nAlice,30\nBob,25"
        expected = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"}
        ]
        self.assertEqual(parse_csv(data), expected)

    def test_parse_csv_empty(self):
        data = ""
        with self.assertRaises(IndexError):
            parse_csv(data)

    def test_save_to_csv(self):
        data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        filename = "test.csv"
        save_to_csv(data, filename)

        with open(filename, "r") as file:
            content = file.read()
        expected = "name,age\nAlice,30\nBob,25\n"
        self.assertEqual(content, expected)

        # Usuwanie testowego pliku
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
