from django.contrib import admin
from .models import Pessoa, TipoPessoa

# Register your models here.
class TipoPessoaAdmin(admin.ModelAdmin):
    list_display = ( 'tipo', 'descricao',)
    list_display_links = ('tipo', 'descricao', )
    list_per_page = 10

admin.site.register(TipoPessoa, TipoPessoaAdmin)
admin.site.register(Pessoa)