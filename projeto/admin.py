from django.contrib import admin
from projeto.models import Cliente,Documento,Meta,Prioridade,Projeto,statusTarefa,Tarefa,Reuniao

admin.site.register(Cliente)
admin.site.register(Projeto)
admin.site.register(statusTarefa)
admin.site.register(Prioridade)
admin.site.register(Tarefa)
admin.site.register(Meta)
admin.site.register(Documento)
admin.site.register(Reuniao)
