from django.urls import path
from . import views

urlpatterns = [
    path('produtos', views.ProdutoIndex.as_view(), name='listar_produtos'),
    path('fornecedores', views.FornecedorIndex.as_view(), name='listar_fornecedores'),
    path('categorias', views.CategoriaIndex.as_view(), name='listar_categorias'),
    path('unidades-medidas', views.UnidadeMedidaIndex.as_view(), name='listar_unidades-medidas'),
    path('tipos', views.TipoIndex.as_view(), name='listar_tipos'),
    path('condicoes', views.CondicaoIndex.as_view(), name='listar_condicoes'),
]
