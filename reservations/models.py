from django.db import models

from profiles.models import Profile
from commerces.models import Commerce
from courts.models import Court
from services.models import Service
from employees.models import Employee


class ReservationState(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    softDelete = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Payment(models.Model):
    paymentMethodId = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True)
    paymentDate = models.DateTimeField()
    refundDate = models.DateTimeField(blank=True, null=True)
    receiptNumber = models.CharField(max_length=100, blank=True, null=True)


class Review(models.Model):
    commerceId = models.ForeignKey(Commerce, on_delete=models.SET_NULL, blank=True, null=True)
    clientId = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField()
    comment = models.TextField()
    reviewDate = models.DateTimeField()
    softDelete = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.commerceId is not None:
            receiver = str(self.commerceId)
        else:
            receiver = str(self.clientId)

        return receiver + ' - ' + str(self.reviewDate.strftime('%d/%m/%y'))
            

class Reservation(models.Model):
    commerceId = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    clientId = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    courtId = models.ForeignKey(Court, on_delete=models.SET_NULL, blank=True, null=True)
    serviceId = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    employeeId = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    paymentId = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    stateId = models.ForeignKey(ReservationState, on_delete=models.SET_NULL, blank=True, null=True)
    clientReviewId = models.ForeignKey(Review, on_delete=models.SET_NULL, blank=True, null=True, related_name='client_review')
    commerceReviewId = models.ForeignKey(Review, on_delete=models.SET_NULL, blank=True, null=True, related_name='commerce_review')
    clientName = models.CharField(max_length=100, blank=True, null=True)
    clientPhone = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    reservationDate = models.DateTimeField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    cancellationDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.commerceId) + ' - ' + str(self.clientId) + ' - ' + str(self.startDate.strftime('%d/%m/%y'))
