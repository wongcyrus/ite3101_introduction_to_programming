import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab10.ch010_t08_part_of_the_whole_ans import get_class_average,lloyd,alice,tyler
        else:
            from lab.lab10.ch010_t08_part_of_the_whole import get_class_average,lloyd,alice,tyler
        self.assertAlmostEqual(83.86666666666666, get_class_average([alice, lloyd, tyler]))


if __name__ == '__main__':
    unittest.main()
