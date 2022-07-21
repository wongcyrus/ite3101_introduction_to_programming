import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab04.ch04_t13_else_ans import black_knight, french_soldier
        else:
            from lab.lab04.ch04_t13_else import black_knight, french_soldier
        self.assertTrue(black_knight())
        self.assertFalse(french_soldier())


if __name__ == '__main__':
    unittest.main()
