import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab.lab11.ch011_t03_append_to_list_ans import n
else:
    from lab.lab11.ch011_t03_append_to_list import n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([1, 3, 5, 4], n)

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t03_append_to_list.py")

        expected = """[1, 3, 5, 4]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
