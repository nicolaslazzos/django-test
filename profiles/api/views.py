from rest_framework import generics

from profiles.models import Profile, Favorite
from commerces.models import Commerce

from .serializers import ProfileReadSerializer, ProfileCreateUpdateSerializer, FavoriteIdSerializer
from commerces.api.serializers import CommerceReadSerializer


# PROFILE VIEWS

class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileReadSerializer
    
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Profile.objects.filter(softDelete__isnull=True)

        email = self.request.query_params.get('email', None)

        if self.is_param_valid(email):
            qs = qs.filter(email=email)

        return qs


class ProfileCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_url_kwarg = 'profileId'
    serializer_class = ProfileCreateUpdateSerializer

    def get_queryset(self):
        qs = Profile.objects.all()
        return qs.filter(softDelete__isnull=True)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    lookup_url_kwarg = 'profileId'
    serializer_class = ProfileReadSerializer

    def get_queryset(self):
        qs = Profile.objects.all()
        return qs.filter(softDelete__isnull=True)


# FAVORITES VIEWS

class FavoriteListAPIView(generics.ListAPIView):
    serializer_class = CommerceReadSerializer

    def get_queryset(self):
        profileId = self.request.query_params.get('profileId', None)
        user_favorites = Favorite.objects.filter(profileId=profileId)
        return Commerce.objects.filter(id__in=user_favorites)


class FavoriteIdListAPIView(generics.ListAPIView):
    serializer_class = FavoriteIdSerializer

    def get_queryset(self):
        profileId = self.request.query_params.get('profileId', None)
        return Favorite.objects.filter(profileId=profileId)


class FavoriteCreateDeleteAPIView(generics.CreateAPIView, generics.DestroyAPIView):
    lookup_url_kwarg = 'id'
    serializer_class = FavoriteIdSerializer

    def get_queryset(self):
        return Favorite.objects.all()
