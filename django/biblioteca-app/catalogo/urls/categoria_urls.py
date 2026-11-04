from django.urls import path
from catalogo.views.categoria_views import (categoria_list, categoria_create )

urlpatterns = [
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/crear/', categoria_create, name='categoria_create'),
]