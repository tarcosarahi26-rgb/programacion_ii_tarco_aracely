from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("saludo", views.saludo, name="saludo"),
    path("greeting/<str:nombre>/",
          views.greeting, name="greeting"),
    path("destination/<str:titulo>/<str:nombre>/<str:cargo>",
              views.destination, name="destinatario"),
    path("base_triangulo/<int:base>/<int:altura>",
                  views.base_triangulo, name="base_triangulo"),
    path("leads-like", views.leads_like, name="leads_like"),
]