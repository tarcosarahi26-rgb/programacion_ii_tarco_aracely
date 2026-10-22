from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, TaskFlow")

def register(request):
    """Resgistro de usuarios."""
    return HttpResponse("Registro de usuarios en linea")

def saludo(request):
    """Saludo a usuarios."""
    return HttpResponse("Bienvenido usuario, te saluda el creador")

def greeting(request, nombre):
    """Saludo a usuarios con entrada."""
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")

def destination(request, titulo, nombre, cargo):
    """Saludo a usuarios."""
    return HttpResponse(f"bienvenido: {titulo} {nombre}, su cargo es: {cargo}")

def base_triangulo(request, base, altura):
    """Saludo a usuarios."""
    return HttpResponse(f"La base es: {base*altura/2}")

def leads_like(request):
    contexto = {
        "titulo": "ESTUDIANTE",
        "nombre": "Aracely ",
        "apellido":"Tarco"
    }
    return render(request, "leads/leads-like.html", 
                  contexto)