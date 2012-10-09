from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Documento,Tarefa,statusTarefa
from projeto_forms.formsTarefa import formDocumento,formStatusTarefa

def index(request):
    return HttpResponse("teste")

'''TAREFA'''
def adicionarStatusTarefa(request):
    if request.method=="POST":
        form=formStatusTarefa(request.POST,request.FILES)

        if form.is_valid():
            dadosStatusTarefa=form.cleaned_data

            objStatusTarefa=statusTarefa(nome=dadosStatusTarefa['nome'])
            objStatusTarefa.save()

            return render_to_response('salvo.html',{})
    else:
        form=formStatusTarefa()

    return render_to_response('adicionar.html',{'form':form})

def excluirTarefa(request,id_tarefa):
    return HttpResponse()

'''DOCUMENTO'''
def adicionarDocumento(request):
    if request.method=="POST":
        formulario=formDocumento(request.POST,request.FILES)
        if formulario.is_valid():
            dadosDocumento=formulario.cleaned_data

            documento=Documento(
                tarefa=Tarefa.objects.get(pk=dadosDocumento['id_tarefa']),
                nome=dadosDocumento['nome'],
                caminho=dadosDocumento['caminho']
            )
            documento.save()

            return render_to_response('salvo.html',{})
    else:
        formulario=formDocumento()

    return render_to_response('adicionar.html',{'form':formulario},context_instance=RequestContext(request))