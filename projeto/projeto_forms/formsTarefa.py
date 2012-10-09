from django import forms
from django.conf.global_settings import FILE_UPLOAD_TEMP_DIR
from django.forms import Select
from PyJaMa.settings import PROJETO_MEDIA
from projeto.models import Tarefa

class formStatusTarefa(forms.Form):
    nome=forms.CharField(max_length=255)

class formPrioridade(forms.Form):
    nome=forms.CharField(max_length=255)

class formTipoTarefa(forms.Form):
    nome=forms.CharField(max_length=255)

class formMeta(forms.Form):
    nome=forms.CharField(max_length=255)
    descricao=forms.CharField()

class formDocumento(forms.Form):
    nome=forms.CharField(max_length=255)
    caminho=forms.FileField()
    tarefa=forms.IntegerField(widget=forms.Select(choices=Tarefa.objects.all().values_list('id','nome')))