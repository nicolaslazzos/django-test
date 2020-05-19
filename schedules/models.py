from django.db import models

from commerces.models import Commerce
from employees.models import Employee


class Schedule(models.Model):
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    reservationMinLength = models.SmallIntegerField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField(blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        name = ''
        if self.employeeId is not None:
            name = str(self.employeeId)
        else:
            name = str(self.commerceId)

        return name + ' - ' + str(self.startDate.strftime('%d/%m/%y'))


class Day(models.Model):
    id = models.SmallIntegerField(primary_key=True, unique=True)
    order = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class WorkShift(models.Model):
    scheduleId = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    firstShiftStart = models.CharField(max_length=5, null=True, blank=True)
    firstShiftEnd = models.CharField(max_length=5, null=True, blank=True)
    secondShiftStart = models.CharField(max_length=5, null=True, blank=True)
    secondShiftEnd = models.CharField(max_length=5, null=True, blank=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.scheduleId)


class ScheduleSetting(models.Model):
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    reservationDayPeriod = models.SmallIntegerField()
    reservationMinCancelTime = models.SmallIntegerField()

    def __str__(self):
        if self.employeeId is not None:
            return str(self.employeeId)
        else:
            return str(self.commerceId)



