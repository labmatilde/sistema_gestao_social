from django.contrib import admin
from .models import Armazenagem, TipoArmazenagem

# Register your models here.
class ArmazenagemAdmin(admin.ModelAdmin):
    list_display = ( 'nome_armazem', 'endereco', 'cep', 'numero', 'tipo', )
    list_display_links = ('nome_armazem', 'endereco', )
    list_per_page = 10

admin.site.register(Armazenagem, ArmazenagemAdmin)
admin.site.register(TipoArmazenagem)