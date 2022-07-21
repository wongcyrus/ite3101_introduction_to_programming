import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t04_not_too_selfish_ans import Animal
        else:
            from lab.lab18.ch018_t04_not_too_selfish import Animal
        self.animal = Animal("Dog")

    def test_member(self):
        self.assertEqual("Dog", self.animal.name)


if __name__ == '__main__':
    unittest.main()
