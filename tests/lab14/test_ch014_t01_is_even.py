import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t01_is_even_ans import is_even
        else:
            from lab.lab14.ch014_t01_is_even import is_even
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))


if __name__ == '__main__':
    unittest.main()
