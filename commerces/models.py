from django.db import models

from provinces.models import Province


class Area(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=300, blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


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
    ratingCount = models.IntegerField(default=0)
    ratingTotal = models.IntegerField(default=0)
    profilePicture = models.URLField(max_length=300, blank=True, null=True)
    headerPicture = models.URLField(max_length=300, blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
