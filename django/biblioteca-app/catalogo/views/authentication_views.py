from calendar import c
import re

from django.conf.locale import te
from django.contrib.auth.views import LoginView, LogoutView
class BibliotecaLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True  
class BibliotecaLogoutView(LogoutView):
    template_name = 'catalogo/logout.html'
    http_method_names = ['get', 'post', 'options']
    next_page = '/'
      