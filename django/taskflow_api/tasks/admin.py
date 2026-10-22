
from django.contrib import admin
from .models import Panaderia, Project


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