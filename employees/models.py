from django.db import models
from django.core.validators import MinValueValidator
from .validators import validate_not_only_digits, validate_has_letter

MIN_AGE = 14

class Employee(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_not_only_digits, validate_has_letter])
    second_name = models.CharField(max_length=100, validators=[validate_not_only_digits, validate_has_letter])
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(MIN_AGE)])
    departments = models.ManyToManyField(
        'Department',
    )
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='employees'
        ordering = ['id']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(age__gte=MIN_AGE),
                name='employee_age_range'
            ),
        ]

    def __str__(self):
        return f'{self.second_name} {self.first_name}'

class Salary(models.Model):
    employee = models.OneToOneField(
        'Employee', 
        on_delete=models.CASCADE
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )

    class Meta:
        db_table='salaries'
        ordering = ['id']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(salary__gte=0),
                name='salary_non_negative'
            ),
        ]

    def __str__(self):
        return f'{self.employee}: {self.salary} BYN'


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table='departments'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'
