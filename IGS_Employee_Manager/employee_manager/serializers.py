from rest_framework import serializers
from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ("id", "name", "employees")
