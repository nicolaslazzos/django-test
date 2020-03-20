from django.db import models

# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name