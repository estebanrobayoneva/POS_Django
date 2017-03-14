from django.shortcuts import render
from .forms import newCategory, newCategoryForm
from .models import Category


# Create your views here.
def index(request):
	form = newCategoryForm(request.POST or None )
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.descripcion:
			instance.descripcion = 'Ninguna'
		instance.save()

#		form_data = form.cleaned_data
#		nombre = form_data.get('nombre')
#		desc = form_data.get('descripcion')
#		obj = Category.objects.create(nombre=nombre, descripcion=desc)
		
#def index(request):
#	form = newCategory(request.POST or None )
#	if form.is_valid():
#		form_data = form.cleaned_data
#		nombre = form_data.get('nombre')
#		desc = form_data.get('descripcion')
#		obj = Category.objects.create(nombre=nombre, descripcion=desc)
		

	context = {
	#'form' es como sera llamado para rederizar en la plantilla(template)
		'form': form,
	}
	return render(request, 'index.html', context)