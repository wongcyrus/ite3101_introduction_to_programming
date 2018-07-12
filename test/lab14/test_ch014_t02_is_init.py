import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab14.ch014_t02_is_init_ans import is_int
else:
    from lab14.ch014_t02_is_init import is_int


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertTrue(is_int(2))
        self.assertTrue(is_int(4))
        self.assertFalse(is_int(1.1))
        self.assertTrue(is_int(0))


if __name__ == '__main__':
    unittest.main()
