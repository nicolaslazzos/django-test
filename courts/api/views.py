from rest_framework import generics
from django.db.models import Q

from courts.models import CourtType, GroundType, Court
from courts.api.serializers import CourtTypeSerializer, GroundTypeSerializer, CourtReadSerializer, CourtCreateUpdateSerializer

class CourtListAPIView(generics.ListAPIView):
    serializer_class = CourtReadSerializer
    lookup_url_kwarg = 'id'

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Court.objects.all().filter(softDelete=None)

        commerceId = self.request.query_params.get('commerceId', None)
        courtTypeId = self.request.query_params.get('courtTypeId', None)
        userSearch = self.request.query_params.get('contains', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(courtTypeId):
            qs = qs.filter(courtTypeId=courtTypeId)

        if self.is_param_valid(userSearch):
            qs = qs.filter(Q(name__icontains=userSearch) | Q(description__icontains=userSearch))

        return qs

class CourtRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CourtReadSerializer

    def get_queryset(self):
        qs = Court.objects.all()
        return qs.filter(softDelete=None)

class CourtCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = CourtCreateUpdateSerializer

    def get_queryset(self):
        qs = Court.objects.all()
        return qs.filter(softDelete=None)

class CourtTypeListAPIView(generics.ListAPIView):
    serializer_class = CourtTypeSerializer

    def get_queryset(self):
        qs = CourtType.objects.all().filter(softDelete=None)
        return qs

class GroundTypeListAPIView(generics.ListAPIView):
    serializer_class = GroundTypeSerializer

    def get_queryset(self):
        qs = GroundType.objects.all().filter(softDelete=None)
        return qs