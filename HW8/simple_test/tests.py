import unittest
from HW8.task_1 import same_elements

# def same_elements(first_set, second_set):
#     res = set()
#     for item in first_set:
#         for element in second_set:
#             if item == element:
#                 res.add(item)
#                 continue
#     if res:
#         return res
#     else:
#         return "There's no same elements in these 2 sets"


class TestSameElements(unittest.TestCase):
    first_set_true = {1, 2, 3, 4}
    second_set_true = {3, 4, 5, 6}
    first_set_false = {0, 1, 2}
    second_set_false = {10, 11, 12}

    def test_same_elements_success(self):
        self.assertEqual(same_elements(self.first_set_true, self.second_set_true), {3, 4})
        self.assertEqual(
            same_elements(self.first_set_false, self.second_set_false),
            "There's no same elements in these 2 sets"
        )

    def test_same_elements_invalid_arguments(self):
        with self.assertRaises(TypeError):
            self.assertEqual(same_elements({1, 2, 3}, (3, 4, 5)), {3})
            self.assertEqual(same_elements(1), "There's no same elements in these 2 sets")
            self.assertEqual({1, 2, 3}, "2, 3, 4")


if __name__ == '__main__':
    unittest.main()
