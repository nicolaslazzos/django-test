from django.db import models

# Create your models here.


class Profile(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    provinceId = models.TextField()

