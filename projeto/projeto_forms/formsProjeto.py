from django import forms
from projeto.models import Projeto, Cliente, Reuniao

class formCliente(forms.ModelForm):
    class Meta:
        model=Cliente

class formProjeto(forms.ModelForm):
    class Meta:
        model=Projeto

class formReuniao(forms.ModelForm):
    class Meta:
        model=Reuniao
