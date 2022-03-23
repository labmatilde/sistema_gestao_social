from django.db import models
from sgdominios.models import Atividade
# from sgfamilia.models import Familia
from sgdominios.models import Status

# Create your models here.
class Pessoa(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    primeiro_nome = models.CharField(max_length=100)
    nome_meio = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    data_nascimento = models.DateField
    email = models.EmailField(max_length=100)
    atividades = models.ManyToManyField(Atividade, blank=False)
    tipo_pessoa = models.ForeignKey('TipoPessoa', null=False, blank=False, on_delete=models.PROTECT)
    # familia = models.ForeignKey(Familia, null=True, blank=True)
    def __str__(self):
        return self.tipo
    
class TipoPessoa(models.Model):
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
        verbose_name = 'Tipo Pessoa'
        verbose_name_plural = 'Tipo Pessoa'