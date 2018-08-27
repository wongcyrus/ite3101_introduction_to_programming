import unittest

from ..console_test_helper import execfile, is_answer

if is_answer:
    from lab.lab11.ch011_t02_list_element_modi_ans import n
else:
    from lab.lab11.ch011_t02_list_element_modi import n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([1, 15, 5], n)
        self.assertAlmostEqual(15, n[1])

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t02_list_element_modi.py")

        expected = """[1, 15, 5]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
