
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='categoria_list', permanent=False), name='home'),
    path('catalogo/', include('catalogo.urls.categoria_urls')),  # Incluye las URLs de la aplicación 'catalogo'
]
