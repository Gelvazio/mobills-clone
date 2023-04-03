from django.urls import path
from receita.views import index, home, listar

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('receitas', listar, name='receitas'),
]