import unittest

from ..console_test_helper import is_answer

if is_answer:
    from lab.lab08.ch08_t01_intro_to_list_ans import zoo_animals
else:
    from lab.lab08.ch08_t01_intro_to_list import zoo_animals


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(4, len(zoo_animals))


if __name__ == '__main__':
    unittest.main()
