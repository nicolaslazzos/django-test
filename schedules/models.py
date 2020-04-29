from django.db import models

from commerces.models import Commerce

# Create your models here.
class Schedule(models.Model):
  commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
  # employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
  startDate = models.DateTimeField(blank=True, null=True)
  endDate = models.DateTimeField(blank=True, null=True)
  softDelete = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return str(self.commerceId) + ' - ' + str(self.startDate.strftime('%d/%m/%y'))

class Day(models.Model):
  order = models.SmallIntegerField()
  name = models.CharField(max_length=20)

  def __str__(self):
    return str(self.name)

class WorkShift(models.Model):
  scheduleId = models.ForeignKey(Schedule, on_delete=models.CASCADE)
  days = models.ManyToManyField(Day)
  firstShiftStart = models.CharField(max_length=5, null=True, blank=True)
  firstShiftEnd = models.CharField(max_length=5, null=True, blank=True)
  secondShiftStart = models.CharField(max_length=5, null=True, blank=True)
  secondShiftEnd = models.CharField(max_length=5, null=True, blank=True)

  def __str__(self):
    return str(self.scheduleId)

