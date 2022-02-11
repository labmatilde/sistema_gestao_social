from django.urls import path
from . import views

urlpatterns = [
    path('produtos', views.hello_sgp),
    path('fornecedores', views.FornecedorIndex.as_view(), name='listar_fornecedores'),
    path('categorias', views.hello_sgp),
    path('unidades-medidas', views.hello_sgp),
    path('tipos', views.hello_sgp),
    path('condicoes', views.hello_sgp),
]
