from django.urls import path

from .views import CommerceListAPIView, CommerceRetrieveUpdateDestroyAPIView, CommerceCreateAPIView, AreaListAPIView, AreaIdListAPIView, CommerceDailyReservationsAPIView, CommerceYearsOfActivityAPIView, CommerceMonthlyEarningsAPIView, CommerceMonthlyReviewsAPIView, CommerceReservedAndCanceledReservationsAPIView, CommerceMostPopularShiftsAPIView

urlpatterns = [
    path('', CommerceListAPIView.as_view(), name='commerce-list'),
    path('create/', CommerceCreateAPIView.as_view(), name='commerce-create'),
    path('areas/', AreaListAPIView.as_view(), name='areas-list'),
    path('areas/id/', AreaIdListAPIView.as_view(), name='areas-id-list'),
    path('daily-reservations/', CommerceDailyReservationsAPIView.as_view(), name='daily-reservations-report'),
    path('years-of-activity/', CommerceYearsOfActivityAPIView.as_view(), name='commerce-years-of-activity'),
    path('monthly-earnings/', CommerceMonthlyEarningsAPIView.as_view(), name='monthly-earnings-report'),
    path('monthly-reviews/', CommerceMonthlyReviewsAPIView.as_view(), name='monthly-reviews-report'),
    path('reserved-canceled-reservations/', CommerceReservedAndCanceledReservationsAPIView.as_view(), name='reserved-canceled-report'),
    path('popular-shifts/', CommerceMostPopularShiftsAPIView.as_view(), name='popular-shifts-report'),
    path('delete/<commerceId>/', CommerceRetrieveUpdateDestroyAPIView.as_view(), name='commerce-delete'),
    path('update/<commerceId>/', CommerceRetrieveUpdateDestroyAPIView.as_view(), name='commerce-update'),
    path('<commerceId>/', CommerceRetrieveUpdateDestroyAPIView.as_view(), name='commerce-read'),
]
