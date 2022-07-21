import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t05_is_prime_ans import is_prime
        else:
            from lab.lab14.ch014_t05_is_prime import is_prime
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(0))


if __name__ == '__main__':
    unittest.main()
