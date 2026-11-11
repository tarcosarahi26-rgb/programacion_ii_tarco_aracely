from os import urandom

from django.urls import path
from catalogo.views.authentication_views import BibliotecaLoginView, BibliotecaLogoutView
urlpatterns = [
    path('login/', BibliotecaLoginView.as_view(), name='auth_login'),
    path('logout/', BibliotecaLogoutView.as_view(), name='logout'), 
]