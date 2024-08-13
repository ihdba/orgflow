from django.contrib import admin

# Register your models here.

from .models import Restaurant, Rating

admin.site.register(Restaurant)
admin.site.register(Rating)