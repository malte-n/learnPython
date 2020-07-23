import unittest
from employee_test import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for Employee"""
    def setUp(self):
        self.test_employee = Employee(first_name="Jan", last_name="Kowalski", annual_salary=50000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertTrue(self.test_employee.annual_salary == 55000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(6000)
        self.assertEqual(self.test_employee.annual_salary, 56000)



if __name__ == '__main__':
    unittest.main()
