from django.db import models
# Create your models here.

class relatorio(models.Model):
    nome=models.CharField(max_length=255)

