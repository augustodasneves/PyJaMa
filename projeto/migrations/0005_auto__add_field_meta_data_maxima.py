# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Meta.data_maxima'
        db.add_column('projeto_meta', 'data_maxima',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 10, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Meta.data_maxima'
        db.delete_column('projeto_meta', 'data_maxima')


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
            'documentoAnexo': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'doc +'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['projeto.DocumentoComentario']"}),
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
            'data_maxima': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 10, 0, 0)'}),
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
            'duracao': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 48, 12, 596145)'}),
            'hora_reuniao': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'participantes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'part +'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.Projeto']", 'null': 'True'}),
            'tarefas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tar +'", 'null': 'True', 'to': "orm['projeto.Tarefa']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "'Reuni\\xc3\\xa3o para '", 'max_length': '255'})
        },
        'projeto.statustarefa': {
            'Meta': {'object_name': 'StatusTarefa'},
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
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.StatusTarefa']"}),
            'tipo_tarefa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projeto.TipoTarefa']"})
        },
        'projeto.tipotarefa': {
            'Meta': {'object_name': 'TipoTarefa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projeto']