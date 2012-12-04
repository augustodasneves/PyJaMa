from reportlab.pdfgen import canvas
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.functional import empty
from django.views.generic.simple import direct_to_template, redirect_to
from PyJaMa.settings import LOGIN_URL
from models import *
from projeto_forms.formsTarefa import *
from projeto_forms.formsProjeto import *
import reportlab

'''TAREFA'''
@login_required
def adicionar(request,nameForm):
    try:
        nameForm=eval('form'+nameForm)
    except:
        raise Http404
    if request.method=="POST":
        form=nameForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return render_to_response('salvo.html',{},context_instance=RequestContext(request))
    else:
        form=nameForm()

    return render_to_response('adicionar.html',{'form':form},context_instance=RequestContext(request))

@login_required
def lista(request,modelo):
    try:
        modeloNome=modelo
        modelo=eval(modelo)
        itens=modelo.objects.all()
    except:
        raise Http404
    return render_to_response('lista.html',{'itens':itens,'modelo':modeloNome},context_instance=RequestContext(request))

@login_required
def excluir(request,modelo,id_pk):
    try:
        modelo=eval(modelo)
        modelo.objects.get(pk=id_pk).delete()
    except:
        raise Http404
    return render_to_response('excluido.html',{},context_instance=RequestContext(request))

@login_required
def editar(request,nameForm,id_pk):
    try:
        objEdicao=eval(nameForm)
        objEdita=objEdicao.objects.get(pk=id_pk)
        objEdicao=objEdicao.objects.get(pk=id_pk).__dict__
        nameForm=eval('form'+nameForm)
    except BaseException:
        raise Http404
    if request.method=="POST":
        form=nameForm(request.POST,request.FILES, instance=objEdita)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html',{},context_instance=RequestContext(request))
    else:
        dadosForm=objEdicao
        form=nameForm(instance=objEdita)
    return render_to_response('adicionar.html',{'form':form},context_instance=RequestContext(request))

@login_required
def detalhe(request,modelo,id_pk):
    try:
        objModelo=eval(modelo)
        dadosModelo=objModelo.objects.get(pk=id_pk)
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
                    if "next" in request.GET.keys():
                        return redirect_to(request,request.GET['next'])
                    else:
                        return direct_to_template(request,'logado.html',{},context_instance = RequestContext(request))
                else:
                    return direct_to_template(request,'deslogado.html',{},context_instance = RequestContext(request))
            else:
                return direct_to_template(request,'deslogado.html',{},context_instance = RequestContext(request))
        else:
            form=AuthenticationForm(request)
            erros="Verifique suas informacoes de acesso"
            data=[form,erros]
            return render_to_response('login.html',{'form':form,'erros':erros},context_instance=RequestContext(request))
    else:
        form=AuthenticationForm(request)
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return render_to_response('deslogado.html',{},context_instance=RequestContext(request))

def index(request):
    if request.user.is_authenticated():
        return redirect_to(request,'/projeto/Tarefa/listar/',{},context_instance = RequestContext(request))
    else:
        return redirect_to(request,'/login/',{},context_instance = RequestContext(request))

@login_required
def relatoriogeral(request,modelo):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    p = canvas.Canvas(response)

    objModelo=eval(modelo)
    dadosModelo=objModelo.objects.all()


    p.drawString(20, 800, "Relatorio Geral")
    valor=775
    for dado in dadosModelo:
        if(hasattr(dado,"titulo")==True):
            dadoDetalhe=dado.titulo
        elif(hasattr(dado,"nome")==True):
            dadoDetalhe=dado.nome
        else:
            dadoDetalhe="Nao foi possivel buscar as informacoes"

        p.drawString(20,valor, dadoDetalhe)
        valor=valor-15



    p.showPage()
    p.save()

    return response