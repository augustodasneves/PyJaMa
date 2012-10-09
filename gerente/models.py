from django.db import models
# Create your models here.

class tipoRelatorio(models.Model):
    nome=models.CharField(max_length=255,null=False)

class relatorio(models.Model):
    nome=models.CharField(max_length=255,null=False)
    data_inicio=models.DateField()
    data_final=models.DateField()
