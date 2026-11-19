from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

MIN_AGE = 14

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(MIN_AGE)])
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
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
    employee = models.ForeignKey(
        Employee, 
        related_name='salary', 
        on_delete=models.CASCADE
    )
    salary = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )

    class Meta:
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
    employee = models.OneToOneField(
        Employee,
        related_name='department', 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.employee})'