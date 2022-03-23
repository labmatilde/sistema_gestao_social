from re import T
from django.db import models
from sgdominios.models import Status
from sgpessoa.models import Pessoa

# Create your models here.
class Familia(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField(Status, blank=False, on_delete=models.PROTECT)
    pessoas = models.ForeignKey(Pessoa, blank=False, null=False, on_delete=models.PROTECT)
    def __str__(self):
        return self.tipo
    