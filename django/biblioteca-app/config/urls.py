
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls.home_urls')),
    path('catalogo/', include('catalogo.urls.categoria_urls')),  # Incluye las URLs de la aplicación 'catalogo'
    path('catalogo/libros/', include('catalogo.urls.libro_urls')),  # Incluye las URLs de la aplicación 'catalogo'
]
