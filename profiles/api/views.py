from rest_framework import generics

from profiles.models import Profile
from .serializers import ProfileReadSerializer, ProfileCreateUpdateSerializer


class ProfileListAPIView(generics.ListAPIView):
    # lookup_field = 'clientId'
    serializer_class = ProfileReadSerializer

    def get_queryset(self):
        qs = Profile.objects.all()
        # qs = Profile.objects.select_related('provinceId')
        return qs.filter(softDelete=None)


class ProfileCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_field = 'clientId'
    serializer_class = ProfileCreateUpdateSerializer

    def get_queryset(self):
        qs = Profile.objects.all()
        return qs.filter(softDelete=None)

    # def post(self, request, *args, **kwargs):
    #   return self.create(request, *args, **kwargs)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'clientId'
    serializer_class = ProfileReadSerializer

    def get_queryset(self):
        qs = Profile.objects.all()
        return qs.filter(softDelete=None)