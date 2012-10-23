# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table('projeto_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('projeto', ['Cliente'])

        # Adding model 'Projeto'
        db.create_table('projeto_projeto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Cliente'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('proprietario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('projeto', ['Projeto'])

        # Adding model 'statusTarefa'
        db.create_table('projeto_statustarefa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('projeto', ['statusTarefa'])

        # Adding model 'Prioridade'
        db.create_table('projeto_prioridade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('projeto', ['Prioridade'])

        # Adding model 'tipoTarefa'
        db.create_table('projeto_tipotarefa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('projeto', ['tipoTarefa'])

        # Adding model 'Meta'
        db.create_table('projeto_meta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('projeto', ['Meta'])

        # Adding model 'DocumentoComentario'
        db.create_table('projeto_documentocomentario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caminho', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal('projeto', ['DocumentoComentario'])

        # Adding model 'Comentario'
        db.create_table('projeto_comentario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricaoComentario', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('projeto', ['Comentario'])

        # Adding M2M table for field documentoAnexo on 'Comentario'
        db.create_table('projeto_comentario_documentoAnexo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comentario', models.ForeignKey(orm['projeto.comentario'], null=False)),
            ('documentocomentario', models.ForeignKey(orm['projeto.documentocomentario'], null=False))
        ))
        db.create_unique('projeto_comentario_documentoAnexo', ['comentario_id', 'documentocomentario_id'])

        # Adding model 'Tarefa'
        db.create_table('projeto_tarefa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('tipo_tarefa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.tipoTarefa'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.statusTarefa'])),
            ('prioridade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Prioridade'], null=True)),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Meta'], null=True)),
            ('proprietario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prop +', to=orm['auth.User'])),
            ('prazo', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_fechamento', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('projeto', ['Tarefa'])

        # Adding M2M table for field responsavel on 'Tarefa'
        db.create_table('projeto_tarefa_responsavel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tarefa', models.ForeignKey(orm['projeto.tarefa'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('projeto_tarefa_responsavel', ['tarefa_id', 'user_id'])

        # Adding M2M table for field comentario on 'Tarefa'
        db.create_table('projeto_tarefa_comentario', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tarefa', models.ForeignKey(orm['projeto.tarefa'], null=False)),
            ('comentario', models.ForeignKey(orm['projeto.comentario'], null=False))
        ))
        db.create_unique('projeto_tarefa_comentario', ['tarefa_id', 'comentario_id'])

        # Adding model 'DocumentoTarefa'
        db.create_table('projeto_documentotarefa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tarefa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Tarefa'], null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('caminho', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
        ))
        db.send_create_signal('projeto', ['DocumentoTarefa'])

        # Adding model 'Reuniao'
        db.create_table('projeto_reuniao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projeto.Projeto'], null=True)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('data_reuniao', self.gf('django.db.models.fields.DateField')()),
            ('hora_reuniao', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('projeto', ['Reuniao'])

        # Adding M2M table for field participantes on 'Reuniao'
        db.create_table('projeto_reuniao_participantes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reuniao', models.ForeignKey(orm['projeto.reuniao'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('projeto_reuniao_participantes', ['reuniao_id', 'user_id'])

        # Adding M2M table for field tarefas on 'Reuniao'
        db.create_table('projeto_reuniao_tarefas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reuniao', models.ForeignKey(orm['projeto.reuniao'], null=False)),
            ('tarefa', models.ForeignKey(orm['projeto.tarefa'], null=False))
        ))
        db.create_unique('projeto_reuniao_tarefas', ['reuniao_id', 'tarefa_id'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table('projeto_cliente')

        # Deleting model 'Projeto'
        db.delete_table('projeto_projeto')

        # Deleting model 'statusTarefa'
        db.delete_table('projeto_statustarefa')

        # Deleting model 'Prioridade'
        db.delete_table('projeto_prioridade')

        # Deleting model 'tipoTarefa'
        db.delete_table('projeto_tipotarefa')

        # Deleting model 'Meta'
        db.delete_table('projeto_meta')

        # Deleting model 'DocumentoComentario'
        db.delete_table('projeto_documentocomentario')

        # Deleting model 'Comentario'
        db.delete_table('projeto_comentario')

        # Removing M2M table for field documentoAnexo on 'Comentario'
        db.delete_table('projeto_comentario_documentoAnexo')

        # Deleting model 'Tarefa'
        db.delete_table('projeto_tarefa')

        # Removing M2M table for field responsavel on 'Tarefa'
        db.delete_table('projeto_tarefa_responsavel')

        # Removing M2M table for field comentario on 'Tarefa'
        db.delete_table('projeto_tarefa_comentario')

        # Deleting model 'DocumentoTarefa'
        db.delete_table('projeto_documentotarefa')

        # Deleting model 'Reuniao'
        db.delete_table('projeto_reuniao')

        # Removing M2M table for field participantes on 'Reuniao'
        db.delete_table('projeto_reuniao_participantes')

        # Removing M2M table for field tarefas on 'Reuniao'
        db.delete_table('projeto_reuniao_tarefas')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'projeto.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'projeto.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'descricaoComentario': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'documentoAnexo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'doc +'", 'symmetrical': 'False', 'to': "orm['projeto.DocumentoComentario']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'projeto.documentocomentario': {
            'Meta': {'object_name': 'DocumentoComentario'},
            'caminho': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'projeto.documentotarefa': {
            'Meta': {'object_name': 'DocumentoTarefa'},
            'caminho': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tarefa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Tarefa']", 'null': 'True', 'blank': 'True'})
        },
        'projeto.meta': {
            'Meta': {'object_name': 'Meta'},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'projeto.prioridade': {
            'Meta': {'object_name': 'Prioridade'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'projeto.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Cliente']"}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'proprietario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'projeto.reuniao': {
            'Meta': {'object_name': 'Reuniao'},
            'data_reuniao': ('django.db.models.fields.DateField', [], {}),
            'hora_reuniao': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'participantes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'part +'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Projeto']", 'null': 'True'}),
            'tarefas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tar +'", 'null': 'True', 'to': "orm['projeto.Tarefa']"})
        },
        'projeto.statustarefa': {
            'Meta': {'object_name': 'statusTarefa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'projeto.tarefa': {
            'Meta': {'object_name': 'Tarefa'},
            'comentario': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+coments'", 'symmetrical': 'False', 'to': "orm['projeto.Comentario']"}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {}),
            'data_fechamento': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Meta']", 'null': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prazo': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'prioridade': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Prioridade']", 'null': 'True'}),
            'proprietario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prop +'", 'to': "orm['auth.User']"}),
            'responsavel': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'resp +'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.statusTarefa']"}),
            'tipo_tarefa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.tipoTarefa']"})
        },
        'projeto.tipotarefa': {
            'Meta': {'object_name': 'tipoTarefa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projeto']