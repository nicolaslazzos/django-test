from django.db import models

from provinces.models import Province
from areas.models import Area

# Create your models here.
class Commerce(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    areaId = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    cuit = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    provinceId = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    profilePicture = models.URLField(max_length=300, blank=True, null=True)
    headerPicture = models.URLField(max_length=300, blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
