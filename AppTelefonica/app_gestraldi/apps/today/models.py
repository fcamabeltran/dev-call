from django.db import models
from apps.production.models import Paises,Carrier,Destino,Ruta,DestinoRiesgo

class RiskRatiosHoy(models.Model):
  Cod_Riesgo         = models.IntegerField(primary_key=True,db_column='raho_cod_riesgo')
  Cod_dato           = models.ForeignKey(DestinoRiesgo,db_column='raho_cod_dato',related_name='cod_dato')
  Fec_riesgo         = models.DateField(blank=True, null=True,db_column='raho_fec_riesgo')
  Cat_dato           = models.CharField(max_length=6,db_column='raho_cat_dato')
  Dia_llamadas       = models.IntegerField(blank=True, null=True,db_column='raho_dia_llamadas')
  Dia_minutos        = models.IntegerField(blank=True,null=True,db_column='raho_dia_minutos')
  Ind_umb_llamadas   = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_umb_llamadas')
  Ind_umb_minutos    = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_umb_minutos')
  Aye_llamadas       = models.IntegerField(blank=True, null=True,db_column='raho_aye_llamadas')
  Aye_minutos        = models.IntegerField(blank=True, null=True,db_column='raho_aye_minutos')
  Ind_aye_llamadas   = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_aye_llamadas')
  Ind_aye_minutos    = models.DecimalField(blank=True,max_digits=19, decimal_places=2,null=True,db_column='raho_ind_aye_minutos')
  Avg_xda_llamadas   = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_avg_xda_llamadas')
  Avg_xda_minutos    = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_avg_xda_minutos')
  Ind_avg_xda_llamadas= models.DecimalField(blank=True, max_digits=19,decimal_places=2,null=True,db_column='raho_ind_avg_xda_llamadas')
  Ind_avg_xda_minutos = models.DecimalField(blank=True,max_digits=19, decimal_places=2,null=True,db_column='raho_ind_avg_xda_minutos')
  Avg_xdp_llamadas    = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_avg_xdp_llamadas')
  Avg_xdp_minutos     = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_avg_xdp_minutos')
  Ind_avg_xdp_llamadas= models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_avg_xdp_llamadas')
  Ind_avg_xdp_minutos = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_avg_xdp_minutos')
  Dst_xda_llamadas    = models.DecimalField(blank=True, max_digits=19, decimal_places=2,null=True,db_column='raho_dst_xda_llamadas')
  Dst_xda_minutos     = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_dst_xda_minutos')
  Ind_dst_xda_llamadas= models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_dst_xda_llamadas')
  Ind_dst_xda_minutos = models.DecimalField(blank=True,max_digits=19, decimal_places=2,null=True,db_column='raho_ind_dst_xda_minutos')
  Dst_xdp_llamadas    = models.DecimalField(blank=True, max_digits=19,decimal_places=2,null=True,db_column='raho_dst_xdp_llamadas')
  Dst_xdp_minutos     = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_dst_xdp_minutos')
  Ind_dst_xdp_llamadas= models.DecimalField(blank=True,max_digits=19, decimal_places=2,null=True,db_column='raho_ind_dst_xdp_llamadas')
  Ind_dst_xdp_minutos = models.DecimalField(blank=True,max_digits=19,decimal_places=2, null=True,db_column='raho_ind_dst_xdp_minutos')
  Where_coho            = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_coho')
  Where_codi            = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_codi')
  Where_tasa            = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_tasa')
  def __str__(self):
    return self.Cat_dato
  class Meta:
    managed = False
    db_table = 'tiws_risk_ratios_hoy'
     
class SumbaseCabXnrodestHoy(models.Model):
  Nume_proceso = models.IntegerField(primary_key=True,db_column='sndh_cab_nume_proceso')
  Fecha = models.DateField(db_column='sndh_cab_fecha')
  Nume_destino = models.CharField(max_length=20,db_column='sndh_cab_nume_destino')
  Dist_pais = models.IntegerField(blank=True, null=True,db_column='sndh_cab_dist_pais')
  Dist_carrier = models.IntegerField(blank=True, null=True,db_column='sndh_cab_dist_carrier')
  Dist_numo = models.IntegerField(blank=True, null=True,db_column='sndh_cab_dist_numo')
  Dist_paisesrisk = models.IntegerField(blank=True, null=True,db_column='sndh_cab_dist_paisesrisk')
  Risk_llamadas = models.IntegerField(blank=True, null=True,db_column='sndh_cab_risk_llamadas')
  Risk_minutos = models.BigIntegerField(blank=True, null=True,db_column='sndh_cab_risk_minutos')
  Suma_llamadas = models.IntegerField(blank=True, null=True,db_column='sndh_cab_suma_llamadas')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column='sndh_cab_suma_minutos')
  Flag_conservar = models.CharField(max_length=1, blank=True, null=True,db_column='sndh_cab_flag_conservar')  
  def __str__(self):
    return self.Nume_destino
  class Meta:
    managed = False
    db_table = 'tiws_sumbase_cab_xnrodest_hoy'

class SumbaseCabXnroorigHoy(models.Model):
  Nume_proceso = models.IntegerField(primary_key=True,db_column='snoh_cab_nume_proceso')
  Fecha = models.DateField(db_column='snoh_cab_fecha')
  Nume_origen = models.CharField(max_length=20,db_column='snoh_cab_nume_origen')
  Dist_pais = models.IntegerField(blank=True, null=True,db_column='snoh_cab_dist_pais')
  Dist_carrier = models.IntegerField(blank=True, null=True,db_column='snoh_cab_dist_carrier')
  Dist_numb = models.IntegerField(blank=True, null=True,db_column='snoh_cab_dist_numb')
  Dist_paisesrisk = models.IntegerField(blank=True, null=True,db_column='snoh_cab_dist_paisesrisk')
  Risk_llamadas = models.IntegerField(blank=True, null=True,db_column='snoh_cab_risk_llamadas')
  Risk_minutos = models.BigIntegerField(blank=True, null=True,db_column='snoh_cab_risk_minutos')
  Suma_llamadas = models.IntegerField(blank=True, null=True,db_column='snoh_cab_suma_llamadas')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column='snoh_cab_suma_minutos')
  Flag_conservar = models.CharField(max_length=1, blank=True, null=True,db_column='snoh_cab_flag_conservar')
  def __str__(self):
    return self.Nume_origen
  class Meta:
    managed = False
    db_table = 'tiws_sumbase_cab_xnroorig_hoy'

class SumbaseDetXnumorigHoy(models.Model):
  Nume_proceso = models.IntegerField(primary_key=True,db_column='snoh_nume_proceso')
  Fecha = models.DateField(db_column='snoh_fecha')
  Numeroorigen = models.CharField(max_length=20,db_column='snoh_numeroorigen')
  Orig_pais = models.CharField(max_length=5,db_column='snoh_orig_pais')
  Orig_area = models.CharField(max_length=10,db_column='snoh_orig_area')
  Ruen_carrier = models.CharField(max_length=5,db_column='snoh_ruen_carrier')
  Ruen_pais = models.CharField(max_length=5,db_column='snoh_ruen_pais')
  Dest_pais = models.CharField(max_length=5,db_column='snoh_dest_pais')
  Dest_area = models.CharField(max_length=10,db_column='snoh_dest_area')
  Rusa_carrier = models.CharField(max_length=5,db_column='snoh_rusa_carrier')
  Rusa_pais = models.CharField(max_length=5,db_column='snoh_rusa_pais')
  Suma_llamadas = models.IntegerField(blank=True, null=True,db_column='snoh_suma_llamadas')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column='snoh_suma_minutos')
  Codi_riesgo = models.IntegerField(blank=True, null=True,db_column='snoh_codi_riesgo')
  Clave = models.CharField(max_length=50, blank=True, null=True,db_column='snoh_clave')
  Flag_conservar = models.CharField(max_length=1, blank=True, null=True,db_column='snoh_flag_conservar')
  def __str__(self):
    return self.Numeroorigen
  class Meta:
    managed = False
    db_table = 'tiws_sumbase_det_xnumorig_hoy'

class SumbaseDetXnumrdestHoy(models.Model):
  Nume_proceso = models.IntegerField(primary_key=True,db_column=' sndh_nume_proceso')
  Fecha = models.DateField(db_column=' sndh_fecha')
  Numerodestino = models.CharField(max_length=20,db_column=' sndh_numerodestino')
  Orig_pais = models.CharField(max_length=5,db_column=' sndh_orig_pais')
  Orig_area = models.CharField(max_length=10,db_column=' sndh_orig_area')
  Ruen_carrier = models.CharField(max_length=5,db_column=' sndh_ruen_carrier')
  Ruen_pais = models.CharField(max_length=5,db_column=' sndh_ruen_pais')
  Dest_pais = models.CharField(max_length=5,db_column=' sndh_dest_pais')
  Dest_area = models.CharField(max_length=10,db_column=' sndh_dest_area')
  Rusa_carrier = models.CharField(max_length=5,db_column=' sndh_rusa_carrier')
  Rusa_pais = models.CharField(max_length=5,db_column=' sndh_rusa_pais')
  Suma_llamadas = models.IntegerField(blank=True, null=True,db_column=' sndh_suma_llamadas')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column=' sndh_suma_minutos')
  Codi_riesgo = models.IntegerField(blank=True, null=True,db_column=' sndh_codi_riesgo')
  Clave = models.CharField(max_length=50, blank=True, null=True,db_column=' sndh_clave')
  Flag_conservar = models.CharField(max_length=1, blank=True, null=True,db_column=' sndh_flag_conservar')
  def __str__(self):
    return self.Numerodestino
  class Meta:
    managed = False
    db_table = 'tiws_sumbase_det_xnumrdest_hoy'#

class consolidadoHoy(models.Model):
  Proceso = models.DateField(primary_key=True,db_column='COHO_PROCESO')
  Orig_pais = models.CharField(max_length=5, null=True,db_column='COHO_ORIG_PAIS')
  Orig_area = models.CharField(max_length=10,db_column='COHO_ORIG_AREA')
  Dest_pais = models.CharField(max_length=5, null=True,db_column='COHO_DEST_PAIS')
  Dest_area = models.CharField(max_length=10, blank=True, null=True,db_column='COHO_DEST_AREA')
  Ruta_entrada = models.CharField(max_length=10, blank=True, null=True,db_column='COHO_RUTA_ENTRADA')
  Ruen_carrier = models.CharField(max_length=5,blank=True, null=True,db_column='COHO_RUEN_CARRIER')
  Ruen_pais = models.CharField( max_length=5,blank=True, null=True,db_column='COHO_RUEN_PAIS')
  Ruen_servicio = models.CharField(max_length=10,db_column='COHO_RUEN_SERVICIO')
  Ruta_salida = models.CharField( max_length=10,blank=True, null=True,db_column='COHO_RUTA_SALIDA')
  Rusa_carrier = models.CharField( max_length=5,blank=True, null=True,db_column='COHO_RUSA_CARRIER')
  Rusa_pais = models.CharField(max_length=5,blank=True, null=True,db_column='COHO_RUSA_PAIS')
  Rusa_servicio = models.CharField(max_length=10,blank=True,db_column='COHO_RUSA_SERVICIO')
  Suma_llamadas = models.BigIntegerField(blank=True, null=True,db_column='COHO_SUMA_LLAMADAS')
  Suma_segundos = models.BigIntegerField (blank=True, null=True,db_column='COHO_SUMA_SEGUNDOS')
  Clave = models.CharField(max_length=50,blank=True,db_column='COHO_CLAVE')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column='COHO_SUMA_MINUTOS')
  def __str__(self):
    return self.Orig_pais
  class Meta:
    managed = False
    db_table = 'tiws_consolidado_hoy'##       

class TasacionSolohoy(models.Model):  
  Secuenciaproceso = models.BigIntegerField(primary_key=True,db_column='tasa_secuenciaproceso')
  Secuenciaregistro = models.BigIntegerField(db_column='tasa_secuenciaregistro')
  Secuenciareproceso = models.BigIntegerField(blank=True, null=True,db_column='tasa_secuenciareproceso')
  Fechahora = models.DateTimeField(db_column='tasa_fechahora')
  Numeroorigen = models.CharField(max_length=20,db_column='tasa_numeroorigen')
  Nuor_pais = models.ForeignKey(Paises, null=True,db_column='tasa_nuor_pais',related_name='paisE')
  Nuor_operador = models.ForeignKey(Carrier, null=True,db_column='tasa_nuor_operador',related_name='carrierE')
  Nuor_ciudad = models.ForeignKey(Destino, null=True,db_column='tasa_nuor_ciudad',related_name='destinoE')
  Nuor_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nuor_servicio')
  Numerodestino = models.CharField(max_length=20,db_column='tasa_numerodestino')
  Nude_pais = models.ForeignKey(Paises, null=True,db_column='tasa_nude_pais',related_name='paisS')
  Nude_operador = models.ForeignKey(Carrier, null=True,db_column='tasa_nude_operador',related_name='carrierS')
  Nude_ciudad = models.ForeignKey(Destino, null=True,db_column='tasa_nude_ciudad',related_name='destinoS')
  Nude_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nude_servicio')
  Numerossee = models.CharField(max_length=20, blank=True, null=True,db_column='tasa_numerossee')
  Rutaentrada = models.ForeignKey(Ruta, null=True,db_column='tasa_rutaentrada',related_name='rutaEntrada')
  Ruen_operador = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_operador')
  ruen_pais = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_pais')
  Ruen_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_servicio')
  Rutasalida = models.ForeignKey(Ruta, null=True,db_column='tasa_rutasalida',related_name='rutaSalida')
  Rusa_operador = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_rusa_operador')
  Rusa_pais = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_rusa_pais')
  Rusa_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_rusa_servicio')
  Prefijo = models.CharField(max_length=8, blank=True, null=True,db_column='tasa_prefijo')
  Segundos = models.IntegerField(db_column='tasa_segundos')
  Modalidad = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_modalidad')
  Seor_serie = models.CharField(max_length=20, blank=True, null=True,db_column='tasa_seor_serie')
  Seor_operador = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_seor_operador')
  Seor_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_seor_servicio')
  Seor_ciudad = models.CharField(max_length=8, blank=True, null=True,db_column='tasa_seor_ciudad')
  Sede_serie = models.CharField(max_length=20, blank=True, null=True,db_column='tasa_sede_serie')
  Sede_operador = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_sede_operador')
  Sede_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_sede_servicio')
  Sede_ciudad = models.CharField(max_length=8, blank=True, null=True,db_column='tasa_sede_ciudad')
  Sse_flag = models.CharField(max_length=1, blank=True, null=True,db_column='tasa_sse_flag')
  Fuente = models.IntegerField(db_column='tasa_fuente')
  Flagcruce = models.IntegerField(blank=True, null=True,db_column='tasa_flagcruce')
  Observacion = models.CharField(max_length=100, blank=True, null=True,db_column='tasa_observacion')
  Match_fecha = models.DateField(blank=True, null=True,db_column='tasa_match_fecha')
  Match_hora = models.CharField(max_length=2, blank=True, null=True,db_column='tasa_match_hora')
  Match_xxxx = models.IntegerField(blank=True, null=True,db_column='tasa_match_xxxx')
  def __str__(self):
    return self.Numeroorigen
  class Meta:
    managed = False
    db_table = 'tiws_tasacion_solohoy'
