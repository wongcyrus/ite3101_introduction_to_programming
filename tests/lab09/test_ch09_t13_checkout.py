import unittest
from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab09.ch09_t13_checkout_ans import compute_bill
        else:
            from lab.lab09.ch09_t13_checkout import compute_bill
        self.assertEqual(5.5, compute_bill(["banana", "orange", "apple"]))
        self.assertEqual(5.5, compute_bill(["banana", "orange"]))
        self.assertEqual(0, compute_bill([]))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t13_checkout.py", globals())

        expected = """5.5
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
