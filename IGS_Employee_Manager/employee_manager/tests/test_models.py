from django.test import TestCase
from rest_framework.test import APIClient
from ..models import Department, Employee


class DepartmentModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Test Department")

    def test_department_creation(self):
        self.assertTrue(isinstance(self.department, Department))
        self.assertEqual(self.department.name, "Test Department")


class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Test Department")
        self.employee = Employee.objects.create(
            name="Test Employee",
            email="test.employee@example.com",
            department=self.department,
        )

    def test_employee_creation(self):
        self.assertTrue(isinstance(self.employee, Employee))
        self.assertEqual(self.employee.name, "Test Employee")
        self.assertEqual(self.employee.email, "test.employee@example.com")
        self.assertEqual(self.employee.department, self.department)


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.create(name="Test Department")
        self.employee = Employee.objects.create(
            name="Test Employee",
            email="test.employee@example.com",
            department=self.department,
        )

    def test_department_list(self):
        response = self.client.get("/api/departments/")
        self.assertEqual(response.status_code, 200)

    def test_employee_list(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, 200)
