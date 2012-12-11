import django.contrib.admin
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from projeto.models import Projeto, Cliente, Reuniao

def boolean_coerce(value):
# value is received as a unicode string
    if str(value).lower() in ( '1', 'true' ):
        return True
    elif str(value).lower() in ( '0', 'false' ):
        return False
    return None

class formCliente(forms.ModelForm):
    class Meta:
        model=Cliente

class formProjeto(forms.ModelForm):
    class Meta:
        model=Projeto

class formReuniao(forms.ModelForm):
    class Meta:
        model=Reuniao