from django.contrib import admin
from .models import Respaldo

# Register your models here.
class TiwsRespaldoadmin(admin.ModelAdmin):
	list_display =('Tabla','Base','Rutaoutput','Prefijooutput','Campoclave','Diasreten_bd','Diasreten_fs','Claveminimaactual')
	search_fields = ('Tabla','Base','Rutaoutput','Prefijooutput','Campoclave','Diasreten_bd','Diasreten_fs','Claveminimaactual')
	actions = ('test_action')

