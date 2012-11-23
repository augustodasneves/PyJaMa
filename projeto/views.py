from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from projeto_forms.formsTarefa import *
from projeto_forms.formsProjeto import *

'''TAREFA'''
def adicionar(request,nameForm):
    try:
        nameForm=eval('form'+nameForm)
    except:
        raise Http404
    if request.method=="POST":
        form=nameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return render_to_response('salvo.html',{})
    else:
        form=nameForm()

    return render_to_response('adicionar.html',{'form':form},context_instance=RequestContext(request))

@login_required
def lista(request,modelo):
    try:
        modelo=eval(modelo)
        itens=modelo.objects.all()
    except:
        raise Http404
    return render_to_response('lista.html',{'itens':itens})

def excluir(request,modelo,id_pk):
    try:
        modelo=eval(modelo)
        modelo.objects.get(pk=id_pk).delete()
    except:
        raise Http404
    return render_to_response('excluido.html')

def editar(request,nameForm,id_pk):
    try:
        objEdicao=eval(nameForm)
        objEdicao=objEdicao.objects.get(pk=id_pk).__dict__
        nameForm=eval('form'+nameForm)
    except BaseException:
        raise Http404
    if request.method=="POST":
        form=nameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html',{})
    else:
        dadosForm=objEdicao
        form=nameForm(dadosForm)
    return render_to_response('adicionar.html',{'form':form},context_instance=RequestContext(request))

def detalhe(request,modelo,id_pk):
    try:
        objModelo=eval(modelo)
        dadosModelo=objModelo.objects.get(pk=id_pk).__dict__
    except:
        raise Http404

    return render_to_response('detalhe.html',{'item':dadosModelo})

def login(request):
    if request.method=="POST":
        formautenticado=AuthenticationForm(data=request.POST)
        if formautenticado.is_valid():
            usuario=authenticate(username=request.POST['username'],password=request.POST['password'])
            if usuario is not None:
                if usuario.is_active:
                    auth_login(request,usuario)
                    return render_to_response('logado.html',{})
                else:
                    return render_to_response('salvo.html',{})
            else:
                return render_to_response('excluido.html')
    else:
        form=AuthenticationForm(request)
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return render_to_response('deslogado.html',{})
