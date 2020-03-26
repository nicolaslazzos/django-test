from rest_framework import generics, mixins

from provinces.models import Province
from .serializers import ProvinceSerializer, ProvinceIdSerializer, ProvinceNameSerializer

class ProvinceCreateListView(mixins.CreateModelMixin, generics.ListAPIView):
  serializer_class = ProvinceSerializer
  
  def get_queryset(self):
    qs = Province.objects.all()
    return qs.filter(softDelete=None)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class ProvinceIdListView(generics.ListAPIView):
  serializer_class = ProvinceIdSerializer
  
  def get_queryset(self):
    qs = Province.objects.all()
    return qs.filter(softDelete=None)

class ProvinceNameListView(generics.ListAPIView):
  serializer_class = ProvinceNameSerializer
  
  def get_queryset(self):
    qs = Province.objects.all()
    return qs.filter(softDelete=None)