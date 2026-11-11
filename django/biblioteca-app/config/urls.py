
from django.contrib import admin
from django.urls import path, include
from catalogo.views.authentication_views import BibliotecaLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', BibliotecaLoginView.as_view(), name='login'),
    path('', include('catalogo.urls.home_urls')),
    path('catalogo/', include('catalogo.urls.categoria_urls')),  # Incluye las URLs de la aplicación 'catalogo'
    path('catalogo/libros/', include('catalogo.urls.libro_urls')),
    path('catalogo/auth/', include('catalogo.urls.authentication_urls')),
    
    
]
