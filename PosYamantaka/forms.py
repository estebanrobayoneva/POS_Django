from django import forms
from .models import Category

class newCategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['nombre', 'descripcion']
	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		#validaciones
		return nombre
		

class newCategory(forms.Form):
	nombre = forms.CharField(max_length=100)
	descripcion = forms.CharField(widget=forms.Textarea)
	
