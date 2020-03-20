from rest_framework import generics, mixins

from provinces.models import Province
from .serializers import ProvinceSerializer

class ProvinceCreateListView(mixins.CreateModelMixin, generics.ListAPIView):
  lookup_field = 'pk'
  serializer_class = ProvinceSerializer
  
  def get_queryset(self):
    qs = Province.objects.all()
    return qs.filter(softDelete=None)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class ProvinceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
  lookup_field = 'pk'
  serializer_class = ProvinceSerializer
  
  def get_queryset(self):
    return Province.objects.all()