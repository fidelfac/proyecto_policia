from __future__ import unicode_literals

from django.db import models
from fields import GeopositionField

# Create your models here.

class Denuncia(models.Model):
	motivo = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=200)
	lugardelhecho = models.CharField(max_length=50)
	fecha = models.DateField('Fecha')
	hora = models.TimeField('Hora')
	latitud = models.FloatField('Latitud')
	longitud = models.FloatField('Longitud')
	
	personalid = models.IntegerField(default = 2)
