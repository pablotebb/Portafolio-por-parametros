from django.shortcuts import render

# Create your views here.

def autodidacta(request):
    return render(request, 'autodidacta/autodidacta.html')