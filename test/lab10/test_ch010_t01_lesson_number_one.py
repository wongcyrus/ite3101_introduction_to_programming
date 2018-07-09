import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab10.ch010_t01_lesson_number_one_ans import *
else:
    from lab10.ch010_t01_lesson_number_one import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertDictEqual({
            "name": "Lloyd",
            "homework": [],
            "quizzes": [],
            "tests": []
        }, lloyd)
        self.assertDictEqual({
            "name": "Alice",
            "homework": [],
            "quizzes": [],
            "tests": []
        }, alice)
        self.assertDictEqual({
            "name": "Tyler",
            "homework": [],
            "quizzes": [],
            "tests": []
        }, tyler)


if __name__ == '__main__':
    unittest.main()
