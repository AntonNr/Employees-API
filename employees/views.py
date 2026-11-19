from django.shortcuts import render

from .models import Employee, Salary, Department
from .serializers import EmployeeSerializer, SalarySerializer, DepartmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class SalaryViewSet(viewsets.ModelViewSet):
    serializer_class = SalarySerializer
    queryset = Salary.objects.select_related('employee')

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.select_related('employee')


