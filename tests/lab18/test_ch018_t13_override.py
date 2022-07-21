import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t13_override_ans import Employee, PartTimeEmployee
        else:
            from lab.lab18.ch018_t13_override import Employee, PartTimeEmployee
        self.employee = Employee("Employee")
        self.part_time_employee = PartTimeEmployee("PartTimeEmployee")

    def test(self):
        self.assertEqual(0, self.employee.calculate_wage(0))
        self.assertEqual(20.0, self.employee.calculate_wage(1))
        self.assertEqual(40.0, self.employee.calculate_wage(2))
        self.assertEqual(60.0, self.employee.calculate_wage(3))
        self.assertEqual(12.0, self.part_time_employee.calculate_wage(1))
        self.assertEqual(24.0, self.part_time_employee.calculate_wage(2))
        self.assertEqual(36.0, self.part_time_employee.calculate_wage(3))


if __name__ == '__main__':
    unittest.main()
