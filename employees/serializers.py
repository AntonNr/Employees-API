from rest_framework import serializers
from .models import Employee, Salary, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "second_name", "age", "departments", "create_date"]
        read_only_fields = ["id","create_date"]

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ["id", "employee", "salary"]
        read_only_fields = ["id"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]
        read_only_fields = ["id"]