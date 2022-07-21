import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab18/ch018_t03_classier_classes.py")
        self.assertIn("def __init__(self):", content)


if __name__ == '__main__':
    unittest.main()
