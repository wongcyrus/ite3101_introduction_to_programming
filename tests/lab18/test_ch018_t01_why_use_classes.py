import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab18.ch018_t01_why_use_classes_ans import lemon, Fruit
else:
    from lab.lab18.ch018_t01_why_use_classes import lemon, Fruit


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.fruit = Fruit("lemon", "yellow", "sour", False)

    def test_member(self):
        self.assertEqual("lemon", self.fruit.name)
        self.assertEqual("yellow", self.fruit.color)
        self.assertEqual("sour", self.fruit.flavor)
        self.assertFalse(self.fruit.poisonous)

    def test_create_instance(self):
        self.assertEqual("lemon", lemon.name)
        self.assertEqual("yellow", lemon.color)
        self.assertEqual("sour", lemon.flavor)
        self.assertFalse(lemon.poisonous)


if __name__ == '__main__':
    unittest.main()
