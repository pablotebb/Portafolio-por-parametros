from django.shortcuts import render

# Create your views here.

def aficion(request):
    return render(request, 'aficiones/aficiones.html')
