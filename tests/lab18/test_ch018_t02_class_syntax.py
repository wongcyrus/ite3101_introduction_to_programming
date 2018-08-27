import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab18.ch018_t02_class_syntax_ans import Animal
else:
    from lab.lab18.ch018_t02_class_syntax import Animal


class TestOutput(unittest.TestCase):

    def test(self):
        Animal()


if __name__ == '__main__':
    unittest.main()
