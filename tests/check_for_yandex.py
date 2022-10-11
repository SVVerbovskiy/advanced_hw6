import unittest
import yandex_service


class TestYaApi(unittest.TestCase):

    def setUp(self):
        print('Запускаем метод SetUp')

    def test_success_create_folder(self):
        self.assertEqual(yandex_service.create_folder('test'), 201)

    def test_passed_create_folder(self):
        self.assertEqual(yandex_service.create_folder('test_passed'), 409)

    def tearDown(self):
        yandex_service.delete_folder('test')
        print('Запускаем метод TearDown')


if __name__ == '__main__':
    unittest.main()