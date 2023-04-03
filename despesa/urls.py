from django.urls import path
from despesa.views import index, home, listar

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('despesas', listar, name='despesas'),
]