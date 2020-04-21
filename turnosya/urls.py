"""
turnosya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('profiles.api.urls', 'api-profiles'), namespace='api-profiles')),
    path('api/provinces/', include(('provinces.api.urls', 'api-provinces'), namespace='api-provinces')),
    path('api/areas/', include(('areas.api.urls', 'api-areas'), namespace='api-areas')),
    path('api/commerces/', include(('commerces.api.urls', 'api-commerces'), namespace='api-commerces')),
    path('api/', include(('courts.api.urls', 'api-courts'), namespace='api-courts'))
]
