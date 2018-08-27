import unittest

from ..console_test_helper import execfile, is_answer

if is_answer:
    from lab.lab11.ch011_t04_remove_from_lists_ans import n
else:
    from lab.lab11.ch011_t04_remove_from_lists import n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([3, 5], n)

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t04_remove_from_lists.py")

        expected = """[3, 5]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
