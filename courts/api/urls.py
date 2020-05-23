from django.urls import path

from .views import CourtListAPIView, CourtCreateRetrieveUpdateDestroyAPIView, CourtCreateRetrieveUpdateDestroyAPIView, CourtTypeListAPIView, CourtTypeIdListAPIView, GroundTypeListAPIView, GroundTypeIdListAPIView

urlpatterns = [
    path('courts/', CourtListAPIView.as_view(), name='courts-list'),
    path('courts/create/', CourtCreateRetrieveUpdateDestroyAPIView.as_view(), name='court-create'),
    path('courts/update/<id>/', CourtCreateRetrieveUpdateDestroyAPIView.as_view(), name='court-update'),
    path('courts/delete/<id>/', CourtCreateRetrieveUpdateDestroyAPIView.as_view(), name='court-delete'),
    path('courts/<id>/', CourtCreateRetrieveUpdateDestroyAPIView.as_view(), name='court-read'),
    path('court-types/', CourtTypeListAPIView.as_view(), name='court-types-list'),
    path('court-types/id/', CourtTypeIdListAPIView.as_view(), name='court-types-id-list'),
    path('ground-types/', GroundTypeListAPIView.as_view(), name='ground-types-list'),
    path('ground-types/id/', GroundTypeIdListAPIView.as_view(), name='ground-types-id-list')
]
