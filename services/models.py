from django.db import models

from employees.models import Employee
from commerces.models import Commerce


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    duration = models.SmallIntegerField()
    price = models.FloatField()
    employeesIds = models.ManyToManyField(Employee, blank=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.commerceId) + ' - ' + str(self.name)
