from django.shortcuts import render

# Create your views here.

def habilidad(request):
    return render(request, 'habilidades/habilidades.html')
