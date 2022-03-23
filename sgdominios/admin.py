from django.contrib import admin
from .models import Status, Atividade

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ( 'type', 'descricao',)
    list_display_links = ('type', 'descricao', )
    list_per_page = 10

admin.site.register(Status, StatusAdmin)
admin.site.register(Atividade)

