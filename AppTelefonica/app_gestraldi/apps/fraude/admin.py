from django.contrib import admin

from apps.fraude.models import Central,Servicio,Paises,Indicadores,Carrier,Ruta,ServiciosEspeciales,Destino,DetalleListas,Errores,Parametros,Prefijos,Catalogo,Servicio,Anomalias,Mensaje,Respaldo,DestinoRiesgo


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


class TiwsIndicadoresadmin(admin.ModelAdmin):
	list_display =('Codigo','Sigla','Descripcion','Umbrales','Estado')
	search_fields = ('Codigo','Sigla','Descripcion','Umbrales','Estado')
	actions = ('test_action')

class TiwsDestinoadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Pais','Observacion')
	search_fields = ('Codigo','Descripcion','Pais','Observacion')
	actions = ('test_action')

class TiwsDetalleListasadmin(admin.ModelAdmin):
	list_display =('Codigo','Dato','Descripcion','Estado')
	search_fields = ('Codigo','Dato','Descripcion','Estado')
	actions = ('test_action')

class TiwsErroresadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Modulo','Usrcreacion','Flgrecuperable')
	search_fields = ('Codigo','Descripcion','Modulo','Usrcreacion','Flgrecuperable')
	actions = ('test_action')

class TiwsParametrosadmin(admin.ModelAdmin):
	list_display =('Dominio','Codigo','Descripcion','Cadena1','Cadena2','Cadena3','Valor1','Valor2','Valor3')
	search_fields = ('Dominio','Codigo','Descripcion','Cadena1','Cadena2','Cadena3','Valor1','Valor2','Valor3')
	actions = ('test_action')

class TiwsPrefijosadmin(admin.ModelAdmin):
	list_display =('Prefijo','Posicion','Longitud','Rutaentrada','Rutasalida','Estado','Agregar','Reemplazar','Quitar','Tipo')
	search_fields = ('Prefijo','Posicion','Longitud','Rutaentrada','Rutasalida','Estado','Agregar','Reemplazar','Quitar','Tipo')
	actions = ('test_action')

class TiwsCatalogoadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Largo','Nivel')
	search_fields = ('Codigo','Descripcion','Largo','Nivel')
	actions = ('test_action')

class TiwsUmbralessadmin(admin.ModelAdmin):
	list_display =('Dominio','Nivel','Descripcion','Largo','Llamadas','Minutos','Cantidad')
	search_fields = ('Dominio','Nivel','Descripcion')
	actions = ('test_action')

class TiwsRutaadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion')
	search_fields = ('Codigo','Descripcion','Central__Descripcion','TipoTrafico')
	actions = ('test_action')

class TiwsServicioadmin(admin.ModelAdmin):
	list_display =('Codigo','Descripcion','Sigla')
	search_fields = ('Codigo','Descripcion','Sigla')
	actions = ('test_action')

class TiwsAnomaliasadmin(admin.ModelAdmin):
	list_display =('Numero','Fecha_Data','Fecha_proceso','Fecha_proceso','Tipo_anomalia','Codi_destinoriesgo')
	search_fields = ('Numero','Fecha_Data','Fecha_proceso','Fecha_proceso','Tipo_anomalia','Codi_destinoriesgo')
	actions = ('test_action')

class TiwsMensajeadmin(admin.ModelAdmin):
	list_display =('Usrdestino','Asunto','Mensaje','Flgleido','Fechor_recepcion','Fechor_envio','Fechor_lectura','Usrorigen')
	search_fields = ('Usrdestino','Asunto','Mensaje','Flgleido','Fechor_recepcion','Fechor_envio','Fechor_lectura','Usrorigen')
	actions = ('test_action')

class TiwsRespaldoadmin(admin.ModelAdmin):
	list_display =('Tabla','Base','Rutaoutput','Prefijooutput','Campoclave','Diasreten_bd','Diasreten_fs','Claveminimaactual')
	search_fields = ('Tabla','Base','Rutaoutput','Prefijooutput','Campoclave','Diasreten_bd','Diasreten_fs','Claveminimaactual')
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
admin.site.register(DetalleListas,TiwsDetalleListasadmin),
admin.site.register(Errores,TiwsErroresadmin),
admin.site.register(Parametros,TiwsParametrosadmin),
admin.site.register(Prefijos,TiwsPrefijosadmin),
admin.site.register(Catalogo,TiwsCatalogoadmin),
admin.site.register(Anomalias,TiwsAnomaliasadmin),
admin.site.register(DestinoRiesgo,TiwsDestinoRiesgoadmin),
admin.site.register(Mensaje,TiwsMensajeadmin),
admin.site.register(Respaldo,TiwsRespaldoadmin),
admin.site.register(ServiciosEspeciales,TiwsServiciosEspecialesadmin),


