

from django.urls import path



from . import views

urlpatterns = [
     path('', views.index, name = 'projects'),
     path('add_project/', views.add_project, name = 'add_project'),
]
