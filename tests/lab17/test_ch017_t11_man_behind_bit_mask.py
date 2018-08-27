import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab17.ch017_t11_man_behind_bit_mask_ans import check_bit4
else:
    from lab.lab17.ch017_t11_man_behind_bit_mask import check_bit4


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual("off", check_bit4(0b1))
        self.assertEqual("on", check_bit4(0b1101))
        self.assertEqual("on", check_bit4(0b1010))


if __name__ == '__main__':
    unittest.main()
