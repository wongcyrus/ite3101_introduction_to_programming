import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab06.ch06_t06_prac_makes_perfect_ans import cube, by_three
        else:
            from lab.lab06.ch06_t06_prac_makes_perfect import cube, by_three
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t06_prac_makes_perfect.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['cube'], types.FunctionType)
        self.assertIsInstance(temp_locals['by_three'], types.FunctionType)
        self.assertEqual(1000, cube(10))
        self.assertEqual(False, by_three(10))
        self.assertEqual(1728, by_three(12))


if __name__ == '__main__':
    unittest.main()
