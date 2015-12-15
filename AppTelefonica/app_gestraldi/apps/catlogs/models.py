from django.db import models

# Create your models here.
class Catalogo(models.Model):
    Codigo = models.IntegerField(primary_key=True,db_column='risk_codigo')
    Descripcion = models.CharField(max_length=20, blank=True, null=True,db_column='risk_descripcion')
    Largo = models.CharField(max_length=100, blank=True, null=True,db_column='risk_largo')
    Nivel = models.IntegerField(blank=True, null=True,db_column='risk_nivel')
    Estado = models.CharField(max_length=1, blank=True, null=True,db_column='risk_estado')
    Funcion = models.CharField(max_length=50, blank=True, null=True,db_column='risk_funcion')
    Tipo_funcion = models.CharField(max_length=20, blank=True, null=True,db_column='risk_tipo_funcion')
    def __str__(self):
     return self.Descripcion
    class Meta:
      managed = False
      db_table = 'TIWS_RISK_CATALOGO'