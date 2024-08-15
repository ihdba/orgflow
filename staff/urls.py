
from django.urls import path



from . import views

urlpatterns = [
     path('', views.index, name = 'staff'),
     path('add_staff', views.add_staff, name = 'add_staff'),
     path('<int:pk>/', views.staff_detail, name = 'staff_detail'),
]
