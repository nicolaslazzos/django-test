from django.db import models

from profiles.models import Profile
from commerces.models import Commerce


class Role(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    value = models.SmallIntegerField()
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    profileId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    inviteDate = models.DateTimeField()
    startDate = models.DateTimeField(blank=True, null=True)
    visible = models.BooleanField(default=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.profileId) + ' - ' + str(self.roleId)
