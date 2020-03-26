from rest_framework import generics, mixins

from areas.models import Area
from .serializers import AreaSerializer, AreaIdSerializer

class AreaCreateListView(mixins.CreateModelMixin, generics.ListAPIView):
  serializer_class = AreaSerializer
  
  def get_queryset(self):
    qs = Area.objects.all()
    return qs.filter(softDelete=None)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class AreaIdListView(generics.ListAPIView):
  serializer_class = AreaIdSerializer
  
  def get_queryset(self):
    qs = Area.objects.all()
    return qs.filter(softDelete=None)