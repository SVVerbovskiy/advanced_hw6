import unittest
import json
import app
from pathlib import Path
from unittest.mock import patch


def update_date():
    f_directories = f'{Path().absolute()}\\fixtures\\directories.json'
    f_documents = f'{Path().absolute()}\\fixtures\\documents.json'
    with open(str(f_directories), 'r') as out_dirs:
        directories = json.load(out_dirs)
    with open(str(f_documents), 'r') as out_docs:
        documents = json.load(out_docs)
    return directories, documents


class TestApp(unittest.TestCase):
    get_name = "2207 876234"
    doc_number = "10006"

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    @patch('builtins.input', return_value=get_name)
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), "Василий Гупкин")

    @patch('builtins.input', side_effect=['7311', 'pass', 'Shamil', 2])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(app.add_new_doc(), 2)

    @patch('builtins.input', return_value=doc_number)
    def test_delete_doc(self, mock_input):
        self.assertTrue(app.delete_doc())


if __name__ == '__main__':
    unittest.main()
