from django.urls import path

from .views import CourtListAPIView, CourtRetrieveAPIView, CourtCreateUpdateAPIView, CourtTypeListAPIView, GroundTypeListAPIView

urlpatterns = [
    path('courts/', CourtListAPIView.as_view(), name='courts-list'),
    path('courts/<id>/', CourtRetrieveAPIView.as_view(), name='court-read'),
    path('courts/create/', CourtCreateUpdateAPIView.as_view(), name='court-create'),
    path('courts/update/<id>/', CourtCreateUpdateAPIView.as_view(), name='court-update'),
    path('court-types/', CourtTypeListAPIView.as_view(), name='court-types-list'),
    path('ground-types/', GroundTypeListAPIView.as_view(), name='ground-types-list')
]
