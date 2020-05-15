from django.db import models

from profiles.models import Profile
from commerces.models import Commerce
from employees.models import Employee
from reservations.models import Reservation

class NotificationToken(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
      return str(self.profileId)


class NotificationType(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    profileId = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    commerceId = models.ForeignKey(Commerce, blank=True, null=True, on_delete=models.CASCADE)
    employeeId = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    reservationId = models.ForeignKey(Reservation, blank=True, null=True, on_delete=models.CASCADE)
    notificationTypeId = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    read = models.BooleanField(default=False)
    date = models.DateTimeField()
    acceptanceDate = models.DateTimeField(blank=True, null=True)
    rejectionDate = models.DateTimeField(blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
      if self.commerceId is not None:
        receiver = str(self.commerceId)
      else:
        receiver = str(self.profileId)

      return receiver + ' - ' + self.title + ' - ' + str(self.date.strftime('%d/%m/%y'))
    
