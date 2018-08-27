import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab10.ch010_t02_what_the_score_ans import *
else:
    from lab.lab10.ch010_t02_what_the_score import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertDictEqual({
            "name": "Lloyd",
            "homework": [90.0, 97.0, 75.0, 92.0],
            "quizzes": [88.0, 40.0, 94.0],
            "tests": [75.0, 90.0]
        }, lloyd)


if __name__ == '__main__':
    unittest.main()
