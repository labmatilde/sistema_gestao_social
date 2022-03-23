from django.db import models
from sgdominios.models import Status

# Create your models here.
class Armazenagem(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    nome_armazem = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    numero = models.IntegerField
    tipo = models.ForeignKey('TipoArmazenagem', null=False, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = 'Armazenagem'
        verbose_name_plural = 'Armazenagens'

class TipoArmazenagem(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = 'Tipo Armazenagem'
        verbose_name_plural = 'Tipo Armazenagens'