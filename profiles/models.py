from django.db import models

from provinces.models import Province
from commerces.models import Commerce

# Create your models here.
class Profile(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    profilePicture = models.URLField(max_length=300, blank=True, null=True)
    provinceId = models.ForeignKey(Province, blank=True, null=True, on_delete=models.SET_NULL)
    commerceId = models.ForeignKey(Commerce, blank=True, null=True, on_delete=models.SET_NULL)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email

class Favorite(models.Model):
    clientId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clientId) + ' - ' + str(self.commerceId)

