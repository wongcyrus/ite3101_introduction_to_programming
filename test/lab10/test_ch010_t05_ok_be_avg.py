import unittest

from unit_test_helper import is_answer

if is_answer:
    from lab10.ch010_t05_ok_be_avg_ans import average
else:
    from lab10.ch010_t05_ok_be_avg import average


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(2.733333333333333, average([3.5, 2.4, 2.3]))


if __name__ == '__main__':
    unittest.main()
