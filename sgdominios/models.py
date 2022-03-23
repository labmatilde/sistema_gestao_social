from django.db import models

# Create your models here.
class Status(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.type
    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

class Atividade(models.Model):
    criando_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.CharField(max_length=100)
    atualizado_por = models.CharField(max_length=100)
    status = models.OneToOneField('Status', blank=False, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo
