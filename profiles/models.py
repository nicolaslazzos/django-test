from django.db import models

# Create your models here.


class Profile(models.Model):
    profileId = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    provinceId = models.CharField(blank=True, null=True, max_length=50)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

