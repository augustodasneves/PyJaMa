from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.conf.urls import patterns, url
from projeto import views
from projeto.projeto_forms.formsProjeto import formProjeto


urlpatterns=patterns('',
    url(r'^$','projeto.views.index',name="home"),
    url(r'(?P<modelo>\w+)/listar/$','projeto.views.lista'),
    url(r'(?P<nameForm>\w+)/adicionar/','projeto.views.adicionar'),
    url(r'(?P<nameForm>\w+)/editar/(?P<id_pk>\d+)','projeto.views.editar'),
    url(r'(?P<modelo>\w+)/excluir/(?P<id_pk>\d+)','projeto.views.excluir'),
    url(r'(?P<modelo>\w+)/detalhe/(?P<id_pk>\d+)','projeto.views.detalhe'),
    url(r'(?P<modelo>\w+)/relatorio/','projeto.views.relatoriogeral'),
)