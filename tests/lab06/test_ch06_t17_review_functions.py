import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab06.ch06_t17_review_functions_ans import shut_down
        else:
            from lab.lab06.ch06_t17_review_functions import shut_down
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t17_review_functions.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['shut_down'], types.FunctionType)
        self.assertEqual("Shutting down", shut_down("yes"))
        self.assertEqual("Shutdown aborted", shut_down("no"))
        self.assertEqual("Sorry", shut_down("other"))


if __name__ == '__main__':
    unittest.main()
