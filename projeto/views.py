from urllib2 import parse_keqv_list
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.http import HttpResponse, Http404, HttpResponseRedirect
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

def excluir(request,modelo,id_pk):
    try:
        objModelo=eval(modelo)
        objModelo=objModelo.objects.get(pk=id_pk).delete()
    except:
        raise Http404

    return render_to_response('excluido.html')
