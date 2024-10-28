from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin
from .models import TextData, DistanceData

admin.site.register(TextData)
admin.site.register(DistanceData)

