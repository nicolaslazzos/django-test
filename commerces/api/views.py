from rest_framework import generics

from commerces.models import Commerce
from .serializers import CommerceReadSerializer, CommerceCreateUpdateSerializer


class CommerceListAPIView(generics.ListAPIView):
    serializer_class = CommerceReadSerializer

    def get_queryset(self):
        qs = Commerce.objects.all()
        return qs.filter(softDelete=None)


class CommerceCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_field = 'commerceId'
    serializer_class = CommerceCreateUpdateSerializer

    def get_queryset(self):
        qs = Commerce.objects.all()
        return qs.filter(softDelete=None)


class CommerceRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'commerceId'
    serializer_class = CommerceReadSerializer

    def get_queryset(self):
        qs = Commerce.objects.all()
        return qs.filter(softDelete=None)
