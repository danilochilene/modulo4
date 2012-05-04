#coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from circulante.catalogo.models import Publicacao

class Participante(models.Model):
    user = models.OneToOneField(User)
    ativo = models.BooleanField(default=True)
    

# Create your models here.

def criar_registro_participante(sender, instance, created, **kwargs):
    if created:
        Participante.objects.create(user=instance)

post_save.connect(criar_registro_participante, sender=User)

class Clube(models.Model):
    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=1024)
    membros = models.ManyToManyField(Participante)

OPCOES_STATUS = [
    ('disponivel', u'disponível'), # disponivel para emprestimo
    ('emprestado', u'emprestado'), # emprestado neste momento
    ('reservado', u'reservado'), # não disponivel para emprestimo
    ('privado', u'privado'), # não disponível e não público
]

class Item(models.Model):
    data_aquisicao = models.DateField()
    publicacao = models.ForeignKey(Publicacao)
    proprietario = models.ForeignKey(Participante)
    status = models.CharField(max_length=16, choices=OPCOES_STATUS, default=OPCOES_STATUS[0][0])
    notas = models.TextField(blank=True)
    
class Emprestimo(models.Model):
    solicitante = models.ForeignKey(Participante)
    publicacao = models.ForeignKey(Publicacao)
    item = models.ForeignKey(Item, null=True)
    datahora_retirada = models.DateTimeField(null=True)
    datahora_devolucao = models.DateTimeField(null=True)
    data_limite_devolucao = models.DateTimeField(null=True)
    notas = models.TextField(blank=True)    
