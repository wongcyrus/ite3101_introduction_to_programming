import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab10.ch010_t06_just_weight_n_see_ans import get_average,lloyd,alice,tyler
        else:
            from lab.lab10.ch010_t06_just_weight_n_see import get_average,lloyd,alice,tyler
        self.assertAlmostEqual(80.55, get_average(lloyd))
        self.assertAlmostEqual(91.14999999999999, get_average(alice))
        self.assertAlmostEqual(79.9, get_average(tyler))


if __name__ == '__main__':
    unittest.main()
