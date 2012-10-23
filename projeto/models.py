# -*- coding: utf-8 -*-#
from datetime import datetime
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

class StatusTarefa(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)

class Prioridade(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)

class TipoTarefa(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255,null=False)

class Meta(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True)

class DocumentoComentario(models.Model):
    def __unicode__(self):
        return self.caminho

    caminho=models.FileField("Documento",upload_to=os.path.join(PROJETO_MEDIA,"documentos"),null=True)


class Comentario(models.Model):
    def __unicode__(self):
        return self.descricaoComentario

    descricaoComentario=models.CharField(verbose_name="Descrição",max_length=1024,null=False,blank=False)
    documentoAnexo=models.ManyToManyField(DocumentoComentario,verbose_name="Documentos em Anexo",related_name="doc +")

class Tarefa(models.Model):
    def __unicode__(self):
        return self.nome

    nome=models.CharField(max_length=255)
    descricao=models.TextField()
    tipo_tarefa=models.ForeignKey(TipoTarefa)
    status=models.ForeignKey(StatusTarefa)
    prioridade=models.ForeignKey(Prioridade,null=True)
    meta=models.ForeignKey(Meta,null=True)
    responsavel=models.ManyToManyField(User,verbose_name="StakeHolders",related_name = 'resp +')
    proprietario=models.ForeignKey(User,related_name = 'prop +')
    prazo=models.DateTimeField(null=True)
    comentario=models.ManyToManyField(Comentario,verbose_name="Notas sobre a tarefa",related_name="+coments")
    data_criacao=models.DateTimeField()
    data_fechamento=models.DateTimeField(null=True)

class DocumentoTarefa(models.Model):
    def __unicode__(self):
        return self.nome

    tarefa=models.ForeignKey(Tarefa,null=True,blank=True)
    nome=models.CharField(max_length=255)
    caminho=models.FileField("Documento",upload_to=os.path.join(PROJETO_MEDIA,"documentos"),null=True)

class Reuniao (models.Model):
    def __unicode__(self):
        return self.titulo

    titulo=models.CharField(max_length=255,blank=False,null=False,default="titDefault")
    participantes=models.ManyToManyField(User,verbose_name="Participantes",related_name='part +')
    projeto=models.ForeignKey(Projeto,null=True)
    tarefas=models.ManyToManyField(Tarefa,verbose_name="Tarefas em Pauta",related_name='tar +',null=True)
    local=models.CharField(max_length=255,null=False)
    data_reuniao=models.DateField(null=False)
    hora_reuniao=models.TimeField(null=False)
    duracao=models.TimeField(default=datetime.now().time)

