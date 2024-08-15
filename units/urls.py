
from django.urls import path



from . import views

urlpatterns = [
     path('', views.index, name = 'units'),
     path('<int:pk>/', views.unit_detail, name = 'unit_detail'),
]
