from django.urls import path
from . import views

app_name = "habilidad"

urlpatterns = [
   
    path("", views.habilidad, name="habilidad"),
    
]