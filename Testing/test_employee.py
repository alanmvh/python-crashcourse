import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee class"""

    def setUp(self):
        self.employee = Employee("Jose", "Lemington", 120000)

    def test_give_default_raise(self):
        """Increases by default 5000 to annual salary"""
        self.employee.give_raise()
        self.assertEqual(125000, self.employee.annual_salary)
    
    def test_give_custom_raise(self):
        """Increases a custom ammount the annual salary"""
        self.employee.give_raise(7000)
        self.assertEqual(127000, self.employee.annual_salary)

unittest.main()

