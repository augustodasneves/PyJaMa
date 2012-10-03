import os
from django.db import models
from django.contrib.auth.models import User
from PyJaMa.settings import MEDIA_ROOT,PROJETO_MEDIA

class Cliente(models.Model):
    nome=models.CharField(max_length=255)
    foto=models.ImageField("Logo Cliente",upload_to=os.path.join(PROJETO_MEDIA,"cliente"),blank=True,null=True)
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField()

class  Projeto(models.Model):
    cliente=models.ForeignKey(Cliente)
    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True)
    foto=models.ImageField("Logo Projeto",upload_to=os.path.join(PROJETO_MEDIA,"projeto"),blank=True,null=True)
    proprietario=models.ForeignKey(User)
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField()

class statusTarefa(models.Model):
    nome=models.CharField(max_length=255)
    
class Prioridade(models.Model):
    nome=models.CharField(max_length=255)

class tipoTarefa(models.Model):
    nome=models.CharField(max_length=255,null=False)
    
class Meta(models.Model):
    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True)
    
class Documento(models.Model):
    nome=models.CharField(max_length=255)

class Tarefa(models.Model):
    nome=models.CharField(max_length=255)
    descricao=models.TextField()
    tipo_tarefa=models.ForeignKey(tipoTarefa)
    status=models.ForeignKey(statusTarefa)
    prioridade=models.ForeignKey(Prioridade,null=True)
    meta=models.ForeignKey(Meta,null=True)
    responsavel=models.ManyToManyField(User,verbose_name="StakeHolders",related_name = 'resp +')
    proprietario=models.ForeignKey(User,related_name = 'prop +')
    prazo=models.DateTimeField(null=True)
    data_criacao=models.DateTimeField()
    data_fechamento=models.DateTimeField(null=True)

class Reuniao(models.Model):
    participantes=models.ManyToManyField(User,verbose_name="Participantes",related_name='part +')
    projeto=models.ForeignKey(Projeto,null=True)
    tarefas=models.ManyToManyField(Tarefa,verbose_name="Tarefas em Pauta",related_name='tar +',null=True)
    local=models.CharField(max_length=255)
    data_reuniao=models.DateField()
    hora_reuniao=models.TimeField()