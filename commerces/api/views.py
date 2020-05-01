from rest_framework import generics
from django.db.models import Q

from commerces.models import Commerce
from .serializers import CommerceReadSerializer, CommerceCreateUpdateSerializer


class CommerceListAPIView(generics.ListAPIView):
    serializer_class = CommerceReadSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Commerce.objects.filter(softDelete__isnull=True)

        areaId = self.request.query_params.get('areaId', None)
        provinceId = self.request.query_params.get('provinceId', None)
        userSearch = self.request.query_params.get('contains', None)

        if self.is_param_valid(areaId):
            qs = qs.filter(areaId=areaId)

        if self.is_param_valid(provinceId):
            qs = qs.filter(provinceId=provinceId)

        if self.is_param_valid(userSearch):
            qs = qs.filter(Q(name__icontains=userSearch) | Q(description__icontains=userSearch))

        return qs


class CommerceCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_url_kwarg = 'commerceId'
    serializer_class = CommerceCreateUpdateSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)


class CommerceRetrieveAPIView(generics.RetrieveAPIView):
    lookup_url_kwarg = 'commerceId'
    serializer_class = CommerceReadSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)
