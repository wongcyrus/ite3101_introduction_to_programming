import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab14.ch014_t07_anti_vowel_ans import anti_vowel
else:
    from lab.lab14.ch014_t07_anti_vowel import anti_vowel


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual("Hy Y!", anti_vowel("Hey You!"))
        self.assertEqual("rvrs", anti_vowel("reverse"))
        self.assertEqual("bc", anti_vowel("abc"))
        self.assertEqual("1234", anti_vowel("1234"))
        self.assertEqual("", anti_vowel(""))


if __name__ == '__main__':
    unittest.main()
