from django.shortcuts import render, get_object_or_404

from despesa.models import Despesa

def index(request):
    # despesas = Despesa.objects.all()
    # return render(request, 'galeria/index.html', {"despesas": despesas, "pagina_atual":"home"})
    return render(request, 'despesa/index.html')

def home(request):
    # despesas = Despesa.objects.all()
    # return render(request, 'galeria/index.html', {"despesas": despesas, "pagina_atual":"home"})
    return render(request, 'despesa/home.html')

def listar(request):

    despesas = Despesa.objects.all().order_by("data")

    print(despesas)

    return render(request, 'despesa/index.html', {"despesas": despesas})


