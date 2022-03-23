from django.db import models
from sgdominios.models import Status
from sgfamilia.models import Familia
from sgkit.models import Kit
from sgpessoa.models import Pessoa

# Create your models here.
class Projeto(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    nome_projeto = models.CharField(max_length=100)
    objetivo_projeto = models.CharField(max_length=255)
    descricao_projeto = models.TextField
    pix_projeto = models.CharField(max_length=40)
    pessoas = models.ManyToManyField(Pessoa, blank=False)
    familias = models.ManyToManyField(Familia, blank=True)
    kits = models.ManyToManyField(Kit, blank=False)

    def __str__(self):
        return self.condicao
    