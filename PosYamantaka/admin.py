from django.contrib import admin

# Register your models here.
from .models import Category, Society, Discount
from .forms import newCategoryForm

#personalizar el modelo en admin
class AdminCategory(admin.ModelAdmin):
	list_display = ['nombre', 'descripcion']
	form = newCategoryForm
	list_display_links = ['nombre']
	list_filter = ['nombre']
	list_editable = ['descripcion']
	search_fields = ['nombre']
	#class Meta:
	#	model = Category
class AdminSociety(admin.ModelAdmin):
	list_display = ['nombre','valor_anual', 'valor_semestral','valor_mensual','descripcion']
	list_display_links = ['nombre']
	list_filter = ['nombre']
	list_editable = ['valor_anual', 'valor_semestral','valor_mensual','descripcion']
	search_fields = ['nombre']

class AdminDiscount(admin.ModelAdmin):
	list_display = ['society','category', 'porcentaje_descuento']
	list_display_links = ['society']
	list_filter = ['society']
	list_editable = ['category', 'porcentaje_descuento']
	search_fields = ['society']
	
		


#agragar modelo a admin
#myModels = [Category, Society, Discount]
#admin.site.register(myModels)
admin.site.register(Category, AdminCategory)
admin.site.register(Society, AdminSociety)
admin.site.register(Discount, AdminDiscount)