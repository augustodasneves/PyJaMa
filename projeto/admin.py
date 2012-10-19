from django.contrib import admin
from projeto.models import Cliente,DocumentoTarefa,DocumentoComentario,Meta,Prioridade,Projeto,StatusTarefa,Tarefa,Reuniao,TipoTarefa, DocumentoComentario, DocumentoTarefa

admin.site.register(Cliente)
admin.site.register(Projeto)
admin.site.register(StatusTarefa)
admin.site.register(Prioridade)
admin.site.register(Tarefa)
admin.site.register(Meta)
admin.site.register(DocumentoTarefa)
admin.site.register(DocumentoComentario)
admin.site.register(Reuniao)
admin.site.register(TipoTarefa)