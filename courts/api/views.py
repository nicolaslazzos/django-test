from rest_framework import generics

from courts.models import CourtType, GroundType, Court
from courts.api.serializers import CourtTypeSerializer, CourtTypeIdSerializer, GroundTypeIdSerializer, GroundTypeSerializer, CourtReadSerializer, CourtCreateUpdateSerializer


class CourtListAPIView(generics.ListAPIView):
    serializer_class = CourtReadSerializer
    lookup_url_kwarg = 'id'

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Court.objects.filter(softDelete=None).order_by('name')

        commerceId = self.request.query_params.get('commerceId', None)
        courtTypeId = self.request.query_params.get('courtTypeId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(courtTypeId):
            qs = qs.filter(courtTypeId=courtTypeId)

        return qs


class CourtRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CourtReadSerializer

    def get_queryset(self):
        return Court.objects.filter(softDelete=None)


class CourtCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = CourtCreateUpdateSerializer

    def get_queryset(self):
        return Court.objects.filter(softDelete=None)


class CourtTypeListAPIView(generics.ListAPIView):
    serializer_class = CourtTypeSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = CourtType.objects.filter(softDelete=None).order_by('name')
        
        commerceId = self.request.query_params.get('commerceId', None)

        if self.is_param_valid(commerceId):
            commerce_courts = Court.objects.filter(softDelete=None, commerceId=commerceId)
            qs = qs.filter(id__in=commerce_courts)

        return qs

class CourtTypeIdListAPIView(generics.ListAPIView):
    serializer_class = CourtTypeIdSerializer

    def get_queryset(self):
        return CourtType.objects.filter(softDelete=None).order_by('name')

class GroundTypeListAPIView(generics.ListAPIView):
    serializer_class = GroundTypeSerializer

    def get_queryset(self):
        return GroundType.objects.filter(softDelete=None).order_by('name')

class GroundTypeIdListAPIView(generics.ListAPIView):
    serializer_class = GroundTypeIdSerializer

    def get_queryset(self):
        return GroundType.objects.filter(softDelete=None).order_by('name')
