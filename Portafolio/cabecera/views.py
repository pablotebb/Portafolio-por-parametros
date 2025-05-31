from django.shortcuts import render

# Create your views here.

def datos_personales(request):
    print("Datos personales")
    return render(request, 'cabecera/cabecera.html')
