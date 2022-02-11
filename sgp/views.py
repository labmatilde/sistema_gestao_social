from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView, BaseListView, MultipleObjectMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.views import View
from sympy import Q
from .models import Fornecedor
from django.core import serializers
from django.http import JsonResponse, HttpResponse


# Create your views here.
# adicionar as rotas da api, seria o equivalente a um controller
def hello_sgp(request):
    return HttpResponse('Modulo SGP')


# class FornecedorIndex(View):
#     model = Fornecedor
#     template_name = 'fornecedores.html'
#     paginate_by = 10
#     context_object_name = 'fornecedores'

#     def get_queryset(self):
#         qs = super().get_queryset()
#         # qs = qs.select_related('nome')
#         # qs = qs.order_by('nome').filter()
#         qs = qs.order_by('id').filter()
#         return qs
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         data = serializers.serialize("json", queryset)
#         return JsonResponse(data, status=200, safe=False)
#     def dispatch(self, request, *args, **kwargs):

#         return super(FornecedorIndex, self).dispatch(request, *args, **kwargs)
#     def render_to_response(self, context):
#         queryset = self.model.objects.all()
#         data = serializers.serialize('json', queryset)
#         return HttpResponse(data, content_type='application/json')


class FornecedorIndex(BaseListView):
    model = Fornecedor
    http_method_names = ['get',]

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        qs = qs.order_by('id').filter()
        return qs


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = serializers.serialize('json', queryset)
        print(queryset)
        return JsonResponse(data, status=200, safe=False)
        # return HttpResponse(data, status=200)
    