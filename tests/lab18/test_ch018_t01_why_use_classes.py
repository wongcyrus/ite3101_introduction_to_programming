import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t01_why_use_classes_ans import Fruit
        else:
            from lab.lab18.ch018_t01_why_use_classes import Fruit
        self.fruit = Fruit("lemon", "yellow", "sour", False)

    def test_member(self):
        self.assertEqual("lemon", self.fruit.name)
        self.assertEqual("yellow", self.fruit.color)
        self.assertEqual("sour", self.fruit.flavor)
        self.assertFalse(self.fruit.poisonous)

    def test_create_instance(self):
        if is_answer:
            from lab.lab18.ch018_t01_why_use_classes_ans import lemon
        else:
            from lab.lab18.ch018_t01_why_use_classes import lemon        
        self.assertEqual("lemon", lemon.name)
        self.assertEqual("yellow", lemon.color)
        self.assertEqual("sour", lemon.flavor)
        self.assertFalse(lemon.poisonous)


if __name__ == '__main__':
    unittest.main()
