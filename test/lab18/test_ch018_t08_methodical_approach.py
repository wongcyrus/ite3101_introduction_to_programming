import unittest
from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import get_function_output

if is_answer:
    from lab18.ch018_t08_methodical_approach_ans import hippo
else:
    from lab18.ch018_t08_methodical_approach import hippo


class TestOutput(unittest.TestCase):

    def test_description(self):
        output, value = get_function_output(lambda: hippo.description())
        expected = f"""{hippo.name}
{hippo.age}
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
