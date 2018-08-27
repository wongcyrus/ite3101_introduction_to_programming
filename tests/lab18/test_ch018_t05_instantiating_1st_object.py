import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab18.ch018_t05_instantiating_1st_object_ans import zebra
else:
    from lab.lab18.ch018_t05_instantiating_1st_object import zebra


class TestOutput(unittest.TestCase):

    def test_zebra(self):
        self.assertEqual("Jeffrey", zebra.name)


if __name__ == '__main__':
    unittest.main()
