from django import forms
from projeto.models import Tarefa, StatusTarefa, Prioridade, TipoTarefa, Meta, DocumentoComentario,DocumentoTarefa, Comentario

class formTarefa(forms.ModelForm):
    class Meta():
        model=Tarefa

class formStatusTarefa(forms.ModelForm):
    class Meta():
        model=StatusTarefa

class formPrioridade(forms.ModelForm):
    class Meta():
        model=Prioridade

class formTipoTarefa(forms.ModelForm):
    class Meta():
        model=TipoTarefa

class formMeta(forms.ModelForm):
    class Meta():
        model=Meta

class formDocumentoTarefa(forms.ModelForm):
    class Meta():
        model=DocumentoTarefa

class formDocumentoComentario(forms.ModelForm):
    class Meta():
        model=DocumentoComentario

class formComentario(forms.ModelForm):
    class Meta():
        model=Comentario