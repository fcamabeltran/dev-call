from django.db import models
from apps.production.models import Errores

class controlProceso(models.Model):
  Central = models.BigIntegerField(primary_key=True,db_column='ctrp_central')
  Resecuencia = models.BigIntegerField(db_column='ctrp_resecuencia')
  Secuncia = models.BigIntegerField(db_column='ctrp_secuencia')
  SecuenciaProceso = models.BigIntegerField(db_column='ctrp_secuenciaproceso')
  Ttfilenombre = models.CharField(max_length=50,db_column='ctrp_ttfilenombre')
  Ttfiletotalregistros = models.BigIntegerField( blank=True, null=True,db_column='ctrp_ttfiletotalregistros')
  Prisecregistro = models.CharField(max_length=50, blank=True, null=True,db_column='ctrp_prisecregistro')
  Ultsecregistro = models.CharField(max_length=50, blank=True, null=True,db_column='ctrp_ultsecregistro')
  Priregfecha = models.DateTimeField( blank=True, null=True,db_column='ctrp_priregfecha')
  Prireghora = models.CharField(max_length=20,db_column='ctrp_prireghora')
  Ultregfecha = models.DateTimeField(blank=True, null=True,db_column='ctrp_ultregfecha')
  Ultreghora = models.CharField(max_length=10, blank=True, null=True,db_column='ctrp_ultreghora')
  Proc_estado = models.CharField(max_length=10, blank=True, null=True,db_column='ctrp_proc_estado')
  Proc_fechorini = models.DateTimeField(blank=True, null=True,db_column='ctrp_proc_fechorini')
  Proc_fechorfin = models.DateTimeField( blank=True, null=True,db_column='ctrp_proc_fechorfin')
  Totaltasacion = models.BigIntegerField(db_column='ctrp_totaltasacion')
  Totalrechazos = models.BigIntegerField( blank=True, null=True,db_column='ctrp_totalrechazos')
  Totalnacional = models.BigIntegerField( blank=True, null=True,db_column='ctrp_totalnacional')
  Totalintentos = models.BigIntegerField(blank=True, null=True,db_column='ctrp_totalintentos')
  Error = models.BigIntegerField(db_column='ctrp_error')
  Totaldesbordes = models.BigIntegerField(blank=True, null=True,db_column='ctrp_totaldesbordes')
  Totalparciales = models.BigIntegerField(blank=True, null=True,db_column='ctrp_totalparciales')
  Totalinternacional = models.BigIntegerField(blank=True, null=True,db_column='ctrp_totalinternacional')
  Totalrebotes = models.BigIntegerField( blank=True, null=True,db_column='ctrp_totalrebotes')
  def __str__(self):
    return self.Ttfilenombre
  class Meta:
    managed = False
    db_table = 'tiws_controlproceso'


class Parametros(models.Model):
  Dominio = models.IntegerField(primary_key='True',db_column='para_dominio')
  Codigo = models.IntegerField(primary_key='True',db_column='para_codigo')
  Descripcion = models.CharField(max_length=50,db_column='para_descripcion')
  Cadena1 = models.CharField(max_length=50, blank=True, null=True,db_column='para_cadena1')
  Cadena2 = models.CharField(max_length=50, blank=True, null=True,db_column='para_cadena2')
  Cadena3 = models.CharField(max_length=50, blank=True, null=True,db_column='para_cadena3')
  Valor1 = models.IntegerField(blank=True, null=True,db_column='para_valor1')
  Valor2 = models.IntegerField(blank=True, null=True,db_column='para_valor2')
  Valor3 = models.IntegerField(blank=True, null=True,db_column='para_valor3')
  Estado = models.NullBooleanField(db_column='para_estado')
  def __str__(self):
    return self.Descripcion
  class Meta:
    managed = False
    db_table = 'TIWS_PARAMETROS'

class Prefijos(models.Model):
  Prefijo = models.CharField(primary_key='True',max_length=8,db_column='pref_prefijo')
  Posicion = models.IntegerField(blank=True, null=True,db_column='pref_posicion')
  Longitud = models.IntegerField(blank=True, null=True,db_column='pref_longitud')
  Rutaentrada = models.CharField(primary_key='True',max_length=20,db_column='pref_rutaentrada')
  Rutasalida = models.CharField(primary_key='True',max_length=20,db_column='pref_rutasalida')
  Estado = models.CharField(max_length=1, blank=True, null=True,db_column='pref_estado')
  Agregar = models.CharField(max_length=5, blank=True, null=True,db_column='pref_agregar')
  Reemplazar = models.CharField(max_length=5, blank=True, null=True,db_column='pref_reemplazar')
  Quitar = models.CharField(max_length=5, blank=True, null=True,db_column='pref_quitar')
  Tipo = models.CharField(max_length=4, blank=True, null=True,db_column='pref_tipo')
  def __str__(self):
    return self.Prefijo
  class Meta:
    managed = False
    db_table = 'TIWS_PREFIJOS'

class Rechazos(models.Model):
  Secuenciaproceso= models.IntegerField(primary_key='true',blank=True,db_column='rech_secuenciaproceso')
  Secuenciaregistro= models.IntegerField(blank=True,db_column='rech_secuenciaregistro')
  Fechahora= models.DateTimeField(blank=True,db_column='rech_fechahora')
  Numeroorigen= models.CharField(blank=True,max_length=20,db_column='rech_numeroorigen')
  Numerodestino= models.CharField(blank=True,max_length=20,db_column='rech_numerodestino')
  Rutaentrada= models.CharField(blank=True,max_length=20,db_column='rech_rutaentrada')
  Rutasalida= models.CharField(blank=True,max_length=20,db_column='rech_rutasalida')
  Ip_entrada= models.CharField(blank=True,max_length=15,db_column='rech_ip_entrada')
  Ip_salida= models.CharField(blank=True,max_length=15,db_column='rech_ip_salida')
  Segundos= models.IntegerField(blank=True,db_column='rech_segundos')
  Salidaparcial= models.IntegerField(blank=True,db_column='rech_salidaparcial')
  Numregparcial= models.IntegerField(blank=True,db_column='rech_numregparcial')
  Error= models.ForeignKey(Errores,blank=True,db_column='rech_error')
  Observacion= models.CharField(blank=True,max_length=100,db_column='rech_observacion')
  Id_call= models.CharField(blank=True,max_length=20,db_column='rech_id_call')
  def __str__(self):
    return self.Numeroorigen
  class Meta:
    managed=False
    db_table="TIWS_RECHAZOS"
