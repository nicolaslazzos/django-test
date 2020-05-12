from django.contrib import admin

from reservations.models import ReservationState, PaymentMethod, Payment, Review, Reservation

admin.site.register(ReservationState)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Reservation)
