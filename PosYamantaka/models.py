from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Modelo de categorias
class Category(models.Model):
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(null=True)


	def _unicode_(self):
		return self.nombre

	def _str_(self):
		return self.nombre
class Society(models.Model):
	"""docstring for Society"""
	nombre = models.CharField(max_length = 200)
	descripcion = models.TextField(null=True, blank=True)
	valor_anual = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True )
	valor_semestral = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	valor_mensual = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	categorias = models.ManyToManyField(Category, through='Discount', blank=True)

	def __unicode__(self):
		return self.nombre
class Discount(models.Model):
	"""docstring for ClassName"""
	society = models.ForeignKey(Society)
	category = models.ForeignKey(Category)
	porcentaje_descuento = models.PositiveIntegerField(null=True, blank=True)
	class Meta:
		unique_together = (('society','category'),)
		

		
