from django.contrib import admin
from .models import Central,Servicio,Paises,Indicadores,Carrier,Ruta,ServiciosEspeciales,Destino,Errores,Servicio,Mensaje,DestinoRiesgo

# Register your models here.
class TiwsCentraladmin(admin.ModelAdmin):
	list_display =('Codigo','Sigla','Descripcion','Ubicacion','PersonaContacto','TelefonoContacto','TelefonoContacto','Prefijo','Sufijo')
	search_fields = ('Codigo','Sigla','Descripcion','Ubicacion','PersonaContacto','TelefonoContacto','TelefonoContacto','Prefijo','Sufijo')
	actions = ('test_action')

class TiwsServicioadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Sigla')
	search_fields = ('Codigo','Descripcion','Sigla')
	actions = ('test_action')

class TiwsPaisesadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Discado','Observacion','Flg')
	search_fields = ('Codigo','Descripcion','Discado','Observacion','Flg')
	actions = ('test_action')
class TiwsCarrieradmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Pais','Observacion')
	search_fields = ('Codigo','Descripcion','Pais__Descripcion','Observacion')
	actions = ('test_action')
	
class TiwsDestinoadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Pais','Observacion')
	search_fields = ('Codigo','Descripcion','Pais','Observacion')
	actions = ('test_action')

class TiwsIndicadoresadmin(admin.ModelAdmin):
	list_display =('Codigo','Sigla','Descripcion','Umbrales','Estado')
	search_fields = ('Codigo','Sigla','Descripcion','Umbrales','Estado')
	actions = ('test_action')

class TiwsErroresadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Modulo','Usrcreacion','Flgrecuperable')
	search_fields = ('Codigo','Descripcion','Modulo','Usrcreacion','Flgrecuperable')
	actions = ('test_action')

class TiwsUmbralessadmin(admin.ModelAdmin):
	list_display =('Dominio','Nivel','Descripcion','Largo','Llamadas','Minutos','Cantidad')
	search_fields = ('Dominio','Nivel','Descripcion')
	actions = ('test_action')


class TiwsRutaadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion')
	search_fields = ('Codigo','Descripcion','Central__Descripcion','TipoTrafico')
	actions = ('test_action')

class TiwsDestinoRiesgoadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Largo','Pais','Carrier','Carrier','Area','Servicio','Nivelderiesgo')
	search_fields = ('Codigo','Descripcion','Largo','Pais__Descripcion','Carrier__Descripcion','Area','Servicio__Descripcion','Nivelderiesgo')
	actions = ('test_action')

class TiwsServiciosEspecialesadmin(admin.ModelAdmin):
	list_display =('Numero','Pais','TipoDestino','Servicio','Operador','FechaInicio','FechaFinal')
	search_fields = ('Numero','Pais','TipoDestino','Servicio','Destino','Operador','FechaInicio','FechaFinal','FechadeUso')
	actions = ('test_action')

admin.site.register(Indicadores,TiwsIndicadoresadmin),
admin.site.register(Carrier,TiwsCarrieradmin),
admin.site.register(Ruta,TiwsRutaadmin),
admin.site.register(Central,TiwsCentraladmin),
admin.site.register(Servicio,TiwsServicioadmin),
admin.site.register(Paises,TiwsPaisesadmin),
admin.site.register(Destino,TiwsDestinoadmin),
admin.site.register(Errores,TiwsErroresadmin),
admin.site.register(DestinoRiesgo,TiwsDestinoRiesgoadmin),
admin.site.register(ServiciosEspeciales,TiwsServiciosEspecialesadmin),