from django.contrib import admin
from .models import Parametros,Prefijos

# Register your models here.
class TiwsParametrosadmin(admin.ModelAdmin):
	list_display =('Dominio','Codigo','Descripcion','Cadena1','Cadena2','Cadena3','Valor1','Valor2','Valor3')
	search_fields = ('Dominio','Codigo','Descripcion','Cadena1','Cadena2','Cadena3','Valor1','Valor2','Valor3')
	actions = ('test_action')

class TiwsPrefijosadmin(admin.ModelAdmin):
	list_display =('Prefijo','Posicion','Longitud','Rutaentrada','Rutasalida','Estado','Agregar','Reemplazar','Quitar','Tipo')
	search_fields = ('Prefijo','Posicion','Longitud','Rutaentrada','Rutasalida','Estado','Agregar','Reemplazar','Quitar','Tipo')
	actions = ('test_action')


admin.site.register(Prefijos,TiwsPrefijosadmin),
admin.site.register(Parametros,TiwsParametrosadmin),
