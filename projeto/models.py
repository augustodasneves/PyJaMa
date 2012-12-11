# -*- coding: utf-8 -*-#
from datetime import datetime
import os
from django.db import models
from django.contrib.auth.models import User
from PyJaMa.settings import PROJETO_MEDIA

class Cliente(models.Model):
    nome=models.CharField(max_length=255)
    foto=models.ImageField("Logo Cliente",upload_to=os.path.join(PROJETO_MEDIA,"cliente"),blank=True,null=True)
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField(verbose_name="Data de Criação")

    def __unicode__(self):
        return self.nome

class  Projeto(models.Model):
    cliente=models.ForeignKey(Cliente)
    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True,verbose_name="Descrição")
    foto=models.ImageField("Logo Projeto",upload_to=os.path.join(PROJETO_MEDIA,"projeto"),blank=True,null=True)
    proprietario=models.ForeignKey(User,verbose_name="Proprietário")
    status=models.BooleanField(blank=False,null=False)
    data_criacao=models.DateTimeField(verbose_name="Data de Criação")

    def __unicode__(self):
        return self.nome

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
    nome=models.CharField(max_length=255)
    descricao=models.TextField(null=True,verbose_name="Descrição")
    data_maxima=models.DateField(null=False,default=datetime.now().date(), verbose_name="Prazo final")

    def __unicode__(self):
        return self.nome

class DocumentoComentario(models.Model):
    caminho=models.FileField("Documento",upload_to=os.path.join(PROJETO_MEDIA,"documentos"),null=True)

    def __unicode__(self):
        return self.caminho


class Comentario(models.Model):
    descricaoComentario=models.CharField(verbose_name="Descrição",max_length=1024,null=False,blank=False)
    documentoAnexo=models.ManyToManyField(DocumentoComentario,verbose_name="Documentos em Anexo",related_name="doc +",null=True,blank=True)

    def __unicode__(self):
        return self.descricaoComentario

class Tarefa(models.Model):
    nome=models.CharField(max_length=255)
    descricao=models.TextField(verbose_name="Descrição")
    tipo_tarefa=models.ForeignKey(TipoTarefa,verbose_name="Tipo da Tarefa")
    status=models.ForeignKey(StatusTarefa,editable=False)
    prioridade=models.ForeignKey(Prioridade,null=True)
    meta=models.ForeignKey(Meta,null=True)
    responsavel=models.ManyToManyField(User,verbose_name="Responsaveis",related_name = 'resp +')
    proprietario=models.ForeignKey(User,related_name = 'prop +')
    prazo=models.DateTimeField(null=True,verbose_name="Prazo de Entrega")
    comentario=models.ManyToManyField(Comentario,verbose_name="Comentários sobre a tarefa",related_name="+coments")
    data_criacao=models.DateTimeField(verbose_name="Data de Criação")
    data_fechamento=models.DateTimeField(null=True,verbose_name="Data de Conclusão")

    def __unicode__(self):
        return self.nome

class DocumentoTarefa(models.Model):
    tarefa=models.ForeignKey(Tarefa,null=True,blank=True)
    nome=models.CharField(max_length=255)
    caminho=models.FileField("Documento",upload_to=os.path.join(PROJETO_MEDIA,"documentos"),null=True)

    def __unicode__(self):
        return self.nome

class Reuniao (models.Model):
    titulo=models.CharField(max_length=255,blank=False,null=False,default="Reunião para ",verbose_name="Finalidade")
    participantes=models.ManyToManyField(User,verbose_name="Participantes",related_name='part +')
    projeto=models.ForeignKey(Projeto,null=True)
    tarefas=models.ManyToManyField(Tarefa,verbose_name="Tarefas em Pauta",related_name='tar +',null=True)
    local=models.CharField(max_length=255,null=False)
    data_reuniao=models.DateField(null=False,verbose_name="Data da Reunião")
    hora_reuniao=models.TimeField(null=False,verbose_name="Horário da Reunião")
    duracao=models.TimeField(default=datetime.now().time,verbose_name="Duração")


    def __unicode__(self):
        return self.titulo

