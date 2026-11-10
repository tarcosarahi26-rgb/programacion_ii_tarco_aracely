from django.urls import path
from catalogo.views.libro_views import (
    create_libro,
    delete_libro,
    libro_list,
    update_libro,
)

urlpatterns = [
    path('', libro_list, name='libro_list'),
    path('crear/', create_libro, name='create_libro'),
    path('<int:pk>/eliminar/', delete_libro, name='delete_libro'),
    path('<int:pk>/editar/', update_libro, name='update_libro')
]