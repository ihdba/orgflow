
from django.urls import path



from . import views

urlpatterns = [
     path('', views.index, name = 'staff'),
     path('add_staff', views.add_staff, name = 'add_staff'),
   
]
