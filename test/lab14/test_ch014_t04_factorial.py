import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab14.ch014_t04_factorial_ans import factorial
else:
    from lab14.ch014_t04_factorial import factorial


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))
        self.assertEqual(6, factorial(3))
        self.assertEqual(24, factorial(4))
        self.assertEqual(3628800, factorial(10))
        self.assertEqual(1, factorial(0))


if __name__ == '__main__':
    unittest.main()
