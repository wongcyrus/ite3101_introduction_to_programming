import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab17.ch017_t11_man_behind_bit_mask_ans import check_bit4
        else:
            from lab.lab17.ch017_t11_man_behind_bit_mask import check_bit4
        self.assertEqual("off", check_bit4(0b1))
        self.assertEqual("on", check_bit4(0b1101))
        self.assertEqual("on", check_bit4(0b1010))


if __name__ == '__main__':
    unittest.main()
