from django.urls import path

from reservations.api.views import PaymentCreateUpdateAPIView, ReservationListAPIView, ReservationCreateUpdateAPIView, ReservationRetrieveAPIView, ReviewListAPIView, ReviewCreateUpdateAPIView, ReviewRetrieveAPIView

urlpatterns = [
  path('reservations/', ReservationListAPIView.as_view(), name='reservations-list'),
  path('reservations/create/', ReservationCreateUpdateAPIView.as_view(), name='reservation-create'),
  path('reservations/update/<id>/', ReservationCreateUpdateAPIView.as_view(), name='reservation-update'),
  path('reservations/<id>/', ReservationRetrieveAPIView.as_view(), name='reservation-read'),
  path('payments/create/', PaymentCreateUpdateAPIView.as_view(), name='payment-create'),
  path('payments/update/<id>/', PaymentCreateUpdateAPIView.as_view(), name='payment-update'),
  path('reviews/', ReviewListAPIView.as_view(), name='reviews-list'),
  path('reviews/create/', ReviewCreateUpdateAPIView.as_view(), name='review-create'),
  path('reviews/update/<id>/', ReviewCreateUpdateAPIView.as_view(), name='review-update'),
  path('reviews/<id>/', ReviewRetrieveAPIView.as_view(), name='review-read'),
]