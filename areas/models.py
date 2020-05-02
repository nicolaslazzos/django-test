from django.db import models


class Area(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=300, blank=True, null=True)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
