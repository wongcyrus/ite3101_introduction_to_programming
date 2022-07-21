import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t15_count_as_you_go.py")

        expected = """Your choices are:
1 pizza
2 pasta
3 salad
4 nachos
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
