from rest_framework import generics, mixins

from profiles.models import Profile
from .serializers import ProfileSerializer

class ProfileCreateListView(mixins.CreateModelMixin, generics.ListAPIView):
  # lookup_field = 'clientId'
  serializer_class = ProfileSerializer
  
  def get_queryset(self):
    qs = Profile.objects.all()
    # qs = Profile.objects.select_related('provinceId')
    return qs.filter(softDelete=None)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
  lookup_field = 'clientId'
  serializer_class = ProfileSerializer
  
  def get_queryset(self):
    qs = Profile.objects.all()
    # qs = Profile.objects.select_related('provinceId')
    return qs.filter(softDelete=None)

  # def get_object(self):
  #   pk = self.kwargs.get('profileId')
  #   return Profiles.objects.get(pk=pk)