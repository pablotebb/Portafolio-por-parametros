from django.urls import path
from . import views

app_name = "autodidacta"

urlpatterns = [
   
    path("", views.autodidacta, name="autodidacta"),
    
]