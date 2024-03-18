import unittest
import pandas as pd
from pandas.errors import EmptyDataError

from app.io.input import input_data_from_file, input_data_with_pandas


class TestInputDataWithPandas(unittest.TestCase):

    def test_norm_file_pandas(self):
        fact_result = input_data_with_pandas("/Users/admin/PycharmProjects/python-for-big-data-and-data-science/"
                                             "project_template/data/for_test_pandas.csv")
        self.assertTrue(isinstance(fact_result, pd.DataFrame))

    def test_not_found_file_pandas(self):
        with self.assertRaises(FileNotFoundError):
            input_data_from_file('data/not_found.csv')

    def test_empty_file_pandas(self):
        with open('/Users/admin/PycharmProjects/python-for-big-data-and-data-science/'
                  'project_template/data/empty_file_pandas.csv', 'w') as file:
            pass
        with self.assertRaises(EmptyDataError):
            input_data_with_pandas('/Users/admin/PycharmProjects/python-for-big-data-and-data-science/'
                                   'project_template/data/empty_file_pandas.csv')


class TestInputDataFromFile(unittest.TestCase):

    def test_not_found_file(self):
        with self.assertRaises(FileNotFoundError):
            input_data_from_file('data/not_found.txt')

    def test_empty_file(self):
        fact_result = input_data_from_file('/Users/admin/PycharmProjects/python-for-big-data-and-data-science'
                                           '/project_template/data/empty_file.txt')
        self.assertEqual(fact_result, '')

    def test_norm_file(self):
        content = 'Simple text for test'
        with open('/Users/admin/PycharmProjects/python-for-big-data-and-data-science'
                  '/project_template/data/simple.txt', 'w') as file:
            file.write(content)
        fact_result = input_data_from_file('/Users/admin/PycharmProjects/python-for-big-data-and-data-science'
                                           '/project_template/data/simple.txt')
        self.assertEqual(fact_result, content)
