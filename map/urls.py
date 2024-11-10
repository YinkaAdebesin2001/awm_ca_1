from django.urls import path

from . import views

 

app_name = 'map'  # Declare the app name for namespacing

 

urlpatterns = [

    path('', views.map_view, name='map_view'),
    path('update_location/', views.update_location, name='update_location'),

]