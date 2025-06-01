from django.urls import path
from . import views

app_name = "aficion"

urlpatterns = [
   
    path("", views.aficion, name="aficion"),
    
]