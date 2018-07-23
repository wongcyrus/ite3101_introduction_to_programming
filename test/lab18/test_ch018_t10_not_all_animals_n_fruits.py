import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab18.ch018_t10_not_all_animals_n_fruits_ans import my_cart
else:
    from lab18.ch018_t10_not_all_animals_n_fruits import my_cart


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(1, len(my_cart.items_in_cart))


if __name__ == '__main__':
    unittest.main()
