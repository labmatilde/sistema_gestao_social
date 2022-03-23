from django.db import models
from sgproduto.models import Produto
from sgdominios.models import Status

# Create your models here.
class Kit(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey('TipoKit', null=False, blank=False, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, blank=False)
    def __str__(self):
        return self.nome

class TipoKit(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
