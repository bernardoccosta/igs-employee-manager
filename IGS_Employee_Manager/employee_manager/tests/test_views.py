from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from employee_manager.models import Department, Employee


class DepartmentTests(APITestCase):
    def setUp(self):
        self.superuser = self.create_superuser()
        self.token = Token.objects.create(user=self.superuser)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def create_superuser(self):
        from django.contrib.auth import get_user_model

        user_model = get_user_model()
        return user_model.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )

    def test_create_department(self):
        url = reverse("department-list")
        data = {"name": "Marketing"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.get().name, "Marketing")

    def test_list_departments(self):
        department = Department.objects.create(name="Marketing")
        url = reverse("department-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], department.name)


class EmployeeTests(APITestCase):
    def setUp(self):
        self.superuser = self.create_superuser()
        self.token = Token.objects.create(user=self.superuser)
        self.department = Department.objects.create(name="Marketing")
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def create_superuser(self):
        from django.contrib.auth import get_user_model

        user_model = get_user_model()
        return user_model.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )

    def test_create_employee(self):
        url = reverse("employee-list")
        data = {
            "name": "José Arantes",
            "email": "jose.arantes@example.com",
            "department": self.department.id,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().name, "José Arantes")

    def test_list_employees(self):
        employee = Employee.objects.create(
            name="José Arantes",
            email="jose.arantes@example.com",
            department=self.department,
        )
        url = reverse("employee-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], employee.name)
