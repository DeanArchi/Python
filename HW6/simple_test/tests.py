import unittest
from HW6.task1 import sum_numbers

# def sum_numbers(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_success(self):
        self.assertEqual(sum_numbers(1, 3, 4, 5, 10), 23)
        self.assertEqual(sum_numbers(-1, -2, -5, 8), 0)

    def test_sum_numbers_invalid_arguments(self):
        with self.assertRaises(TypeError):
            self.assertEqual(sum_numbers(1, [1, 2, 3]), 7)
            self.assertEqual(sum_numbers(2, 3, '4'), 9)


if __name__ == '__main__':
    unittest.main()
