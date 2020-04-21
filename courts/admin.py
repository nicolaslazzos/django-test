from django.contrib import admin

from courts.models import CourtType, GroundType, Court

# Register your models here.
admin.site.register(CourtType)
admin.site.register(GroundType)
admin.site.register(Court)
