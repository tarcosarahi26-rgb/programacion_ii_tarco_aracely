from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")

def register(request):
    """Registro de usuarios"""
    
    return HttpResponse("Registro de Usuarios en línea")

def about_me(request):
    """Acerca de usuarios"""
    return HttpResponse("Aracely")