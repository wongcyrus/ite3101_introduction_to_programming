import unittest

from ..console_test_helper import execfile, is_answer

if is_answer:
    from lab.lab11.ch011_t10_modi_ele_of_list_in_func_ans import list_function, n
else:
    from lab.lab11.ch011_t10_modi_ele_of_list_in_func import list_function, n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([3, 11, 7], list_function(n))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t10_modi_ele_of_list_in_func.py")

        expected = """[3, 8, 7]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
