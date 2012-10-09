from django import forms
from projeto.models import Tarefa, statusTarefa, Prioridade, tipoTarefa, Meta, Documento

class formStatusTarefa(forms.ModelForm):
    class Meta():
        model=statusTarefa

class formPrioridade(forms.ModelForm):
    class Meta():
        model=Prioridade

class formTipoTarefa(forms.ModelForm):
    class Meta():
        model=tipoTarefa

class formMeta(forms.ModelForm):
    class Meta():
        model=Meta

class formDocumento(forms.ModelForm):
    class Meta():
        model=Documento