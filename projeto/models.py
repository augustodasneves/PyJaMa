import os
from django.db import models
from django.contrib.auth.models import User
from PyJaMa.settings import PROJETO_MEDIA

class Cliente(models.Model):

    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)
    foto=models.ImageField("Logo Cliente",upload_to=os.path.join(PROJETO_MEDIA,"cliente"),blank=True,null=True)
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField()

class  Projeto(models.Model):

    def __unicode__(self):
        return self.nome

    cliente=models.ForeignKey(Cliente)
    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True)
    foto=models.ImageField("Logo Projeto",upload_to=os.path.join(PROJETO_MEDIA,"projeto"),blank=True,null=True)
    proprietario=models.ForeignKey(User)
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField()

class statusTarefa(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)
    
class Prioridade(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)

class tipoTarefa(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255,null=False)
    
class Meta(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True)

class Tarefa(models.Model):
    def __unicode__(self):
        return self.nome

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

class Documento(models.Model):
    def __unicode__(self):
        return self.nome

    tarefa=models.ForeignKey(Tarefa,null=True,blank=True)
    nome=models.CharField(max_length=255)
    caminho=models.FileField("Documento",upload_to=os.path.join(PROJETO_MEDIA,"documentos"),null=True)

class Reuniao (models.Model):
    def __unicode__(self):
        return self.local

    participantes=models.ManyToManyField(User,verbose_name="Participantes",related_name='part +')
    projeto=models.ForeignKey(Projeto,null=True)
    tarefas=models.ManyToManyField(Tarefa,verbose_name="Tarefas em Pauta",related_name='tar +',null=True)
    local=models.CharField(max_length=255)
    data_reuniao=models.DateField()
    hora_reuniao=models.TimeField()