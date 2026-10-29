from django.shortcuts import redirect, render

from ..forms import ProjectForm, TaskForm
from ..models import Project


def lista(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "home.html", contexto)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project-list")
    else:
        form = TaskForm()

    return render(request, "tasks_form.html", {"form": form, "modo": "crear"})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:project")
    else:
        form = ProjectForm()

    return render(request, "tasks/projects_form.html", {"form": form, "modo": "crear"})