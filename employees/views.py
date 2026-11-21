from django.shortcuts import render

from .models import Employee, Salary, Department
from .serializers import EmployeeSerializer, SalarySerializer, DepartmentSerializer
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class SalaryViewSet(viewsets.ModelViewSet):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


