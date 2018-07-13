import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab17.ch017_t14_slip_n_slide_ans import flip_bit
else:
    from lab17.ch017_t14_slip_n_slide import flip_bit


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(bin(0b10), flip_bit(0b11, 1))
        self.assertEqual(bin(0b1111), flip_bit(0b1101, 2))
        self.assertEqual(bin(0b1110), flip_bit(0b1010, 3))


if __name__ == '__main__':
    unittest.main()
