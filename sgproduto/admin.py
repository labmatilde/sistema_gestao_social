from django.contrib import admin
from .models import Produto, Fornecedor, Categoria, UnidadeMedida, Tipo, Condicao, AtivoFixo

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'data_validade', 'condicao', 'quantidade', )
    list_display_links = ('nome', 'data_validade', )
    list_per_page = 10
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ( 'nome', )
    list_display_links = ('nome', )
    list_per_page = 10
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ( 'categoria', )
    list_display_links = ('categoria', )
    list_per_page = 10
class UnidadeMedidaAdmin(admin.ModelAdmin):
    list_display = ( 'unidade_medida', 'valor_unidade', )
    list_display_links = ('unidade_medida', 'valor_unidade', )
    list_per_page = 10
class TipoAdmin(admin.ModelAdmin):
    list_display = ( 'tipo', )
    list_display_links = ('tipo', )
    list_per_page = 10
class CondicaoAdmin(admin.ModelAdmin):
    list_display = ( 'codicao',)
    list_display_links = ('codicao', )
    list_per_page = 10

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(UnidadeMedida)
admin.site.register(Tipo)
admin.site.register(Condicao)
admin.site.register(AtivoFixo)
