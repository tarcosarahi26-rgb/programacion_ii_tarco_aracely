from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")
