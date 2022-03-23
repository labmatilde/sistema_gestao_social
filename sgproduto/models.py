from dataclasses import Field
from datetime import datetime
from django.db import models
from django.utils import timezone
from sgarmazenagem.models import Armazenagem
from sgdominios.models import Status

# Create your models here.
class Produto(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    foto_produto = models.TextField
    descricao = models.CharField(max_length=100)
    armazenagens = models.ManyToManyField(Armazenagem, blank=False)
    preco = models.DecimalField
    categorias = models.ManyToManyField('Categoria', blank=False)
    tipo = models.ForeignKey('Tipo', null=False, blank=False, on_delete=models.PROTECT)
    perecivel = models.BooleanField()
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
    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        
class Categoria(models.Model):
    ccriando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

class UnidadeMedida(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    unidade_medida = models.CharField(max_length=100)
    valor_unidade = models.CharField(max_length=100)
    def __str__(self):
        return self.unidade_medida

class Tipo(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, verbose_name='status', blank=False, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo

class Condicao(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    condicao = models.CharField(max_length=100)
    def __str__(self):
        return self.condicao
    class Meta:
        verbose_name = 'Condição'
        verbose_name_plural = 'Condições'

class AtivoFixo(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    codigo_ativo = models.CharField(max_length=12)
    produto = models.ForeignKey('Produto', null=False, blank=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.condicao
    class Meta:
        verbose_name = 'Ativos Fixo'
        verbose_name_plural = 'Ativos Fixo'