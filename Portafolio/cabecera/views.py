from django.shortcuts import render

# Create your views here.

def datos_personales(request):
    return render(request, 'cabecera/cabecera.html')
