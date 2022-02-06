from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# adicionar as rotas da api, seria o equivalente a um controller
def hello_sgf(request):
    return HttpResponse('Modulo SGF')