from django.shortcuts import render, get_object_or_404

from receita.models import Receita

def index(request):
    return render(request, 'receita/index.html')

def home(request):
    return render(request, 'receita/home.html')

def listar(request):

    receitas = Receita.objects.all().order_by("data")

    return render(request, 'receita/index.html', {"receitas": receitas})


