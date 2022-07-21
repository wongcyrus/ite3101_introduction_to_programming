import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer

class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t01_before_we_begin_ans import answer
        else:
            from lab.lab07.ch07_t01_before_we_begin import answer
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t01_before_we_begin.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['answer'], types.FunctionType)
        self.assertEqual(42, answer())


if __name__ == '__main__':
    unittest.main()
