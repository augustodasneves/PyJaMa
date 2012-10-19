from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from projeto_forms.formsTarefa import *
from projeto_forms.formsProjeto import *

def index(request):
    return HttpResponse("teste")

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

def lista(request,modelo):
    try:
        modelo=eval(modelo)
    except:
        raise Http404
    itens=modelo.objects.all()
    return render_to_response('lista.html',{'itens':itens})

def excluir(request,modelo,id_pk):
    try:
        modelo=eval(modelo)
    except:
        raise Http404
    modelo.objects.get(pk=id_pk).delete()
    return render_to_response('excluido.html')

def editar(request,nameForm,id_pk):
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