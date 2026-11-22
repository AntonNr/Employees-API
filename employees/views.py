from django.db.models import StringAgg, Value
from .models import Employee, Salary, Department
from .serializers import EmployeeSerializer, SalarySerializer, DepartmentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'departments':
            queryset = queryset.annotate(
                department_names=StringAgg(
                    'departments__name',
                    Value(', '),
                    distinct=True,
                    order_by='departments__name',
                )
            )
        return queryset

    @action(detail=True, methods=['get'], url_path='departments')
    def departments(self, request, pk=None):
        employee = self.get_object()

        return Response({
            'departments': employee.department_names or '',
        })


class SalaryViewSet(viewsets.ModelViewSet):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


