import unittest
from app.io.input import input_data_from_file


class TestInputDataFromFile(unittest.TestCase):

    def test_not_found_file(self):
        with self.assertRaises(FileNotFoundError):
            input_data_from_file('data/not_found.txt')

    def test_empty_file(self):
        with open('data/empty_file.txt', 'w') as file:
            pass
        fact_result = input_data_from_file('data/empty_file.txt')
        self.assertEqual(fact_result, '')

    def test_norm_file(self):
        content = 'Simple text for test'
        with open('data/simple.txt', 'w') as file:
            file.write(content)
        fact_result = input_data_from_file('data/simple.txt')
        self.assertEqual(fact_result,content)

