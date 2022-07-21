import unittest
from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import get_function_output




class TestOutput(unittest.TestCase):

    def test_description(self):
        if is_answer:
            from lab.lab18.ch018_t08_methodical_approach_ans import hippo
        else:
            from lab.lab18.ch018_t08_methodical_approach import hippo
        output, value = get_function_output(lambda: hippo.description())
        expected = f"""{hippo.name}
{hippo.age}
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
