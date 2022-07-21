import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab18.ch018_t02_class_syntax_ans import Animal
        else:
            from lab.lab18.ch018_t02_class_syntax import Animal
        Animal()


if __name__ == '__main__':
    unittest.main()
