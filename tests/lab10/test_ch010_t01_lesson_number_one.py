import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab10.ch010_t01_lesson_number_one_ans import lloyd,alice,tyler
        else:
            from lab.lab10.ch010_t01_lesson_number_one import lloyd,alice,tyler
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
