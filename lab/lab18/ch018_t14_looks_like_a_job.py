class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name: str):
        self.hours = 0
        self.employee_name = employee_name

    def calculate_wage(self, hours: int):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours: int):
        self.hours = hours
        return hours * 12.00

    # Add your code below!
