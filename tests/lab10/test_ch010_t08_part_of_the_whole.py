import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab10.ch010_t08_part_of_the_whole_ans import *
else:
    from lab.lab10.ch010_t08_part_of_the_whole import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(83.86666666666666, get_class_average([alice, lloyd, tyler]))


if __name__ == '__main__':
    unittest.main()
