from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from drf_yasg.utils import swagger_auto_schema


class BaseViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class DepartmentViewSet(BaseViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(BaseViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @swagger_auto_schema(operation_description="Adicionar um novo funcionário")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Listar todos os funcionários")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Remover um funcionário pelo ID")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "employee_list.html", context)
