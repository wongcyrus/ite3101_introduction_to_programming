import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab19.ch019_t11_build_useful_classes_ans import Point3D, my_point
        else:
            from lab.lab19.ch019_t11_build_useful_classes import Point3D, my_point
        self.assertIsInstance(my_point, Point3D)
        self.assertEqual(1, my_point.x)
        self.assertEqual(2, my_point.y)
        self.assertEqual(3, my_point.z)
        self.assertEqual("(1, 2, 3)", str(my_point))


if __name__ == '__main__':
    unittest.main()
