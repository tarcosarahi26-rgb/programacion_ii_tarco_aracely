from django.urls import path
from catalogo.views.home_views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('catalogo/catalogo/', home_view, name='catalogo_home'),
]