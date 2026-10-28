from django.contrib import admin
from .models import Panaderia, Project, Task



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Panaderia)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "tipo_panes",
        "utencilios_cocina",
        "ingredientes",
        "create_at")
    search_fields = ("name",)



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")