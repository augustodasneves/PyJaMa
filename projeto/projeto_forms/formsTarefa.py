from django.contrib.admin.helpers import AdminForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, ReadOnlyPasswordHashField
import django.contrib.auth
import django
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from projeto.models import Tarefa, StatusTarefa, Prioridade, TipoTarefa, Meta, DocumentoComentario,DocumentoTarefa, Comentario

class formTarefa(forms.ModelForm):
    class Meta():
        model=Tarefa
        widgets = {
            'yes_or_no': forms.RadioSelect
        }


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

class formUser(forms.ModelForm):
    class Meta():
        model=User
        fields = ('first_name', 'last_name', 'username', 'email','password')
        exclude = ('is_staff', 'is_active', 'date_joined', 'last_login')

class formUserEditar(UserChangeForm):
    class Meta():
        fields = ('first_name', 'last_name', 'username', 'email','password')

class formLogin(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'Label':'Usuario'}))
    password = forms.CharField(widget=PasswordInput(attrs={'Label':'Senha'}))