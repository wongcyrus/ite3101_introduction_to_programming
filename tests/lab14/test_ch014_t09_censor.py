import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t09_censor_ans import censor
        else:
            from lab.lab14.ch014_t09_censor import censor
        self.assertEqual("this **** is wack ****", censor("this hack is wack hack", "hack"))
        self.assertEqual("reverse", censor("reverse", "se"))
        self.assertEqual("abc * *", censor("abc a a ", "a"))
        self.assertEqual("** 13 ** ** 13 13", censor("12 13 12 12 13 13", "12"))
        self.assertEqual("", censor("", "12"))


if __name__ == '__main__':
    unittest.main()
