from django.urls import path
from . import views

app_name = "cabecera"

urlpatterns = [
   
    path("", views.datos_personales, name="datos_personales"),
    
]