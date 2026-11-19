from django.contrib import admin
from .models import Employee, Salary, Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'second_name', 'first_name', 'age', 'create_date']
    search_fields = ['second_name', 'first_name']
    readonly_fields = ['create_date']

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'salary']
    list_select_related = ['employee']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employee']
    list_select_related = ['employee']
    search_fields = ['name']
    list_filter = ['name']
