

from django.urls import path, include



from . import views

urlpatterns = [

     path('', views.index, name = 'portal'),
     path('staff/', include('staff.urls')),
     path('units/', include('units.urls')),
     path('orm/', include('orm.urls')),
]
