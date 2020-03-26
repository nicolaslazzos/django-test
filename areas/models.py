from django.db import models

# Create your models here.
class Area(models.Model):
    areaId = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
