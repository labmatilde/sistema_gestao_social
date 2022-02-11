from dataclasses import Field
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey('Tipo', null=False, blank=False, on_delete=models.PROTECT)
    perecivel = models.BooleanField()
    categorias = models.ManyToManyField('Categoria', blank=False)
    data_validade = models.DateField()
    ean = models.CharField(max_length=100)
    ncm = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    fornecedor = models.ForeignKey('Fornecedor', null=False, blank=False, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=100)
    data_fabricacao = models.DateField()
    observacao = models.CharField(max_length=100)
    peso_liquido = models.CharField(max_length=100)
    peso_bruto = models.CharField(max_length=100)
    unidade_medida = models.ForeignKey('UnidadeMedida', null=False, blank=False, on_delete=models.PROTECT)
    altura = models.CharField(max_length=100)
    comprimento = models.CharField(max_length=100)
    largura = models.CharField(max_length=100)
    condicao = models.ForeignKey('Condicao', null=False, blank=False, on_delete=models.PROTECT)
    imagem = models.TextField
    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.categoria

class UnidadeMedida(models.Model):
    unidade_medida = models.CharField(max_length=100)
    valor_unidade = models.CharField(max_length=100)
    def __str__(self):
        return self.unidade_medida

class Tipo(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

class Condicao(models.Model):
    codicao = models.CharField(max_length=100)
    def __str__(self):
        return self.codicao
