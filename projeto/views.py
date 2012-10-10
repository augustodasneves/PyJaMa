from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.test._doctest import _OutputRedirectingPdb
from models import *
from projeto_forms.formsTarefa import *

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

def excluirTarefa(request,id_tarefa):
    return HttpResponse()
