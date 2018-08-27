import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab18.ch018_t14_looks_like_a_job_ans import Employee, PartTimeEmployee
else:
    from lab.lab18.ch018_t14_looks_like_a_job import Employee, PartTimeEmployee


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Employee")
        self.part_time_employee = PartTimeEmployee("PartTimeEmployee")

    def test(self):
        self.assertEqual(20.0, self.part_time_employee.full_time_wage(1))
        self.assertEqual(40.0, self.part_time_employee.full_time_wage(2))
        self.assertEqual(60.0, self.part_time_employee.full_time_wage(3))


if __name__ == '__main__':
    unittest.main()
