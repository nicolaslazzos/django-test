from django.db import models

from commerces.models import Commerce


class CourtType(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=300, blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class GroundType(models.Model):
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Court(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    courtTypeId = models.ForeignKey(CourtType, on_delete=models.CASCADE)
    groundTypeId = models.ForeignKey(GroundType, on_delete=models.CASCADE)
    price = models.FloatField()
    lightPrice = models.FloatField(blank=True, null=True)
    lightHour = models.CharField(max_length=5, null=True, blank=True)
    disabledFrom = models.DateTimeField(blank=True, null=True)
    disabledTo = models.DateTimeField(blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.commerceId) + ' - ' + str(self.name)
