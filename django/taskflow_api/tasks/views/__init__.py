from django.http import HttpResponse
from django.shortcuts import render

from .tasks import lista, project_create, task_create


def home(request):
    return HttpResponse("Hola, TaskFlow")


def register(request):
    return HttpResponse("Registro de usuarios en línea")


def about_me(request):
    return HttpResponse("Acerca de mí - Creado por Alison Bermeo")


def greeting(request, nombre):
    return HttpResponse(f"Hola {nombre}, bienvenido a TaskFlow")


def destination(request, titulo, nombre, cargo):
    return HttpResponse(f"Bienvenido: {titulo} {nombre}, su cargo es: {cargo}")


def base_triangulo(request, base, altura):
    area = (base * altura) / 2
    return HttpResponse(f"El área del triángulo es: {area}")


def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "my_firts_template.html", contexto)


def leads_like(request):
    contexto = {
        "titulo": "Programador",
        "nombre": "Alison",
        "apellido": "Bermeo",
    }
    return render(request, "leads-like.html", contexto)