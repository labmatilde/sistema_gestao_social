from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView, BaseListView, MultipleObjectMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.views import View
from sympy import Q
from .models import Fornecedor, Produto, Categoria, UnidadeMedida, Tipo, Condicao
from django.core import serializers
from django.http import JsonResponse, HttpResponse


# Create your views here.
# adicionar as rotas da api, seria o equivalente a um controller
def hello_sgp(request):
    return HttpResponse('Modulo SGP')

class ProdutoIndex(ListView):
    model = Produto
    template_name = 'produto.html'
    paginate_by = 10
    context_object_name = 'produtos'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        print(qs.model)
        return qs

class FornecedorIndex(ListView):
    model = Fornecedor
    template_name = 'fornecedor.html'
    paginate_by = 10
    context_object_name = 'fornecedores'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs

class CategoriaIndex(ListView):
    model = Categoria
    template_name = 'categoria.html'
    paginate_by = 10
    context_object_name = 'categorias'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs

class UnidadeMedidaIndex(ListView):
    model = UnidadeMedida
    template_name = 'unidade-medida.html'
    paginate_by = 10
    context_object_name = 'unidade_medidas'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs

class TipoIndex(ListView):
    model = Tipo
    template_name = 'tipo.html'
    paginate_by = 10
    context_object_name = 'tipos'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs

class CondicaoIndex(ListView):
    model = Condicao
    template_name = 'condicao.html'
    paginate_by = 10
    context_object_name = 'condicoes'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs




# Exemplo de retorno em api
# class FornecedorIndex(BaseListView):
#     model = Fornecedor
#     http_method_names = ['get',]

#     def get_queryset(self):
#         qs = super().get_queryset()
#         # qs = qs.select_related('nome')
#         qs = qs.order_by('id').filter()
#         return qs


#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         data = serializers.serialize('json', queryset)
#         print(queryset)
#         return JsonResponse(data, status=200, safe=False)
#         # return HttpResponse(data, status=200)
    