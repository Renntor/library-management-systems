import os
from cgitb import reset

from utils import add_book, get_book, retrieve_book, delete_book, update_book
import json

from unittest.mock import patch
import unittest


class TestFunctional(unittest.TestCase):

    def setUp(self):
        self.data_base = 'test.json'
        with open(self.data_base, 'w', encoding='utf-8') as file:
            file.write(
                """[
  {
    "title": "test",
    "author": "test",
    "year": 1948,
    "status": "в наличии",
    "id": 1
  }
]"""
            )

    def test_get_book(self):
        result = get_book(self.data_base)
        with open(self.data_base, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        self.assertEqual(
            result,
            f'Список книг: {json.dumps(json_data, indent=2, ensure_ascii=False)}\n'
        )

    @patch('builtins.input', side_effect=['test', 'test', '1948'])
    def test_add_book(self, mock_input):
        result = add_book(self.data_base)
        with open(self.data_base, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        self.assertEqual(
            result,
            f'Книга успешно добавлена{json.dumps(json_data, indent=2, ensure_ascii=False)}\n'
        )

    @patch('builtins.input', side_effect=['year', '1948'])
    def test_retrieve_book(self, mock_input):
        result = retrieve_book(self.data_base)
        with open(self.data_base, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        self.assertEqual(
            result,
            f'Список найденных книг: {json.dumps(json_data, indent=2, ensure_ascii=False)}\n'
        )

    @patch('builtins.input', side_effect=['1', 'выдана'])
    def test_update_book(self, mock_input):
        result = update_book(self.data_base)
        with open(self.data_base, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        self.assertEqual(
            result,
            f'Книга обновлена {json.dumps(json_data[0], indent=2, ensure_ascii=False)}'
        )

    @patch('builtins.input', side_effect=['1'])
    def test_delete_book(self, mock_input):
        result = delete_book(self.data_base)
        self.assertEqual(
            result,
            'Книга удалена\n'
        )

    def tearDown(self):
        os.remove(self.data_base)
