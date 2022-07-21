import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab10.ch010_t03_put_it_together_ans import students
        else:
            from lab.lab10.ch010_t03_put_it_together import students
        self.assertListEqual([{'name': 'Lloyd', 'homework': [90.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0],
                               'tests': [75.0, 90.0]},
                              {'name': 'Alice', 'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0],
                               'tests': [89.0, 97.0]},
                              {'name': 'Tyler', 'homework': [0.0, 87.0, 75.0, 22.0], 'quizzes': [0.0, 75.0, 78.0],
                               'tests': [100.0, 100.0]}], students)


if __name__ == '__main__':
    unittest.main()
