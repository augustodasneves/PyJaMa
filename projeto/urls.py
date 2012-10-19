from django.conf.urls import patterns, url
from django.conf import settings
from projeto.views import adicionar,index,lista
from projeto.projeto_forms.formsTarefa import formStatusTarefa

urlpatterns=patterns('',
    url(r'^$', 'projeto.views.index', name='index'),
    url(r'(?P<modelo>\w+)/listar/$','projeto.views.lista',name="Listar"),
    url(r'(?P<nameForm>\w+)/adicionar/','projeto.views.adicionar',name="Adicionar"),
    url(r'(?P<nameForm>\w+)/editar/(?P<id_pk>)','projeto.views.editar',name="Editar"),
    url(r'(?P<modelo>\w+)/excluir/(?P<id_pk>)','projeto.views.excluir',name="Excluir"),
)