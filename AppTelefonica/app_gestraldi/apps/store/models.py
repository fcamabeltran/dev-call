from django.db import models
from apps.production.models import DestinoRiesgo

# Create your models here.
class Anomalias(models.Model):
 Numero    = models.CharField(primary_key=True,max_length=10,db_column='cano_nume_anomalia')  
 Fecha_Data   = models.DateField(db_column='cano_fecha_data')    
 Fecha_proceso    = models.DateTimeField(db_column='cano_fecha_proceso')    
 Tipo_anomalia    = models.CharField(max_length=10,db_column='cano_tipo_anomalia')   
 Codi_destinoriesgo    = models.IntegerField(db_column='cano_codi_destinoriesgo')   
 Orig_pais    = models.CharField(max_length=5,db_column='cano_orig_pais')    
 Orig_area    = models.CharField(max_length=10,db_column='cano_orig_area')    
 Dest_pais    = models.CharField(max_length=5,db_column='cano_dest_pais')    
 Dest_area    = models.CharField(max_length=10,db_column='cano_dest_area')     
 Ruta_entrada    = models.CharField(max_length=10,db_column='cano_ruta_entrada')   
 Ruen_carrier    = models.CharField(max_length=5,db_column='cano_ruen_carrier')    
 Ruen_pais    = models.CharField(max_length=5,db_column='cano_ruen_pais')    
 Ruen_servicio    = models.CharField(max_length=10,db_column='cano_ruen_servicio')     
 Ruta_salida    = models.CharField(max_length=10,db_column='cano_ruta_salida')    
 Rusa_carrier    = models.CharField(max_length=5,db_column='cano_rusa_carrier')    
 Rusa_pais    = models.CharField(max_length=5,db_column='cano_rusa_pais')   
 Rusa_servicio    = models.CharField(max_length=10,db_column='cano_rusa_servicio')    
 Nume_origen    = models.CharField(max_length=20,db_column='cano_nume_origen')    
 Nume_destino    = models.CharField(max_length=20,db_column='cano_nume_destino')    
 Suma_llamadas    = models.IntegerField(db_column='cano_suma_llamadas')     
 Suma_minutos    = models.IntegerField(default='0',db_column='cano_suma_minutos')     
 def __str__(self):
   return self.Tipo_anomalia 
 class Meta:
   managed = False
   db_table = 'TIWS_CAB_ANOMALIAS'

class RiskTraficoCab(models.Model):
 Proceso = models.IntegerField(primary_key=True,blank=False,db_column='trca_proceso')
 Cod_riesgo = models.IntegerField( blank=False,db_column='trca_cod_riesgo')
 #Cod_dato = models.IntegerField(blank=False,db_column='trca_cod_dato')
 Cod_dato= models.ForeignKey(DestinoRiesgo,db_column='trca_cod_dato',related_name='destinoEs')
 Fec_riesgo = models.DateField(blank=True, null=True,db_column='trca_fec_riesgo')
 Cat_dato = models.CharField(blank=True,max_length=6,db_column='trca_cat_dato')
 Dia_llamadas = models.IntegerField(blank=True, null=True,db_column='trca_dia_llamadas')
 Dia_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_dia_minutos')
 Ind_umb_llamadas = models.DecimalField(blank=True, max_digits=10,decimal_places=3, null=True,db_column='trca_ind_umb_llamadas')
 Ind_umb_minutos = models.DecimalField(blank=True, max_digits=10,decimal_places=3, null=True,db_column='trca_ind_umb_minutos')
 Aye_llamadas = models.DecimalField(blank=True, max_digits=10,decimal_places=3, null=True,db_column='trca_aye_llamadas')
 Aye_minutos = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_aye_minutos')
 Ind_aye_llamadas = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_ind_aye_llamadas')
 Ind_aye_minutos = models.DecimalField(blank=True, max_digits=10,decimal_places=3, null=True,db_column='trca_ind_aye_minutos')
 Avg_xda_llamadas = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_avg_xda_llamadas')
 Avg_xda_minutos = models.DecimalField(blank=True,  max_digits=10,decimal_places=3,null=True,db_column='trca_avg_xda_minutos')
 Ind_avg_xda_llamadas = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_ind_avg_xda_llamadas')
 Ind_avg_xda_minutos = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_ind_avg_xda_minutos')
 Avg_xdp_llamadas = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_avg_xdp_llamadas')
 Avg_xdp_minutos = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_avg_xdp_minutos')
 Ind_avg_xdp_llamadas = models.DecimalField(blank=True,max_digits=10,  decimal_places=3,null=True,db_column='trca_ind_avg_xdp_llamadas')
 Ind_avg_xdp_minutos = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_ind_avg_xdp_minutos')
 Dst_xda_llamadas = models.DecimalField(blank=True,max_digits=10,decimal_places=3, null=True,db_column='trca_dst_xda_llamadas')
 Dst_xda_minutos = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_dst_xda_minutos')
 Ind_dst_xda_llamadas = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_ind_dst_xda_llamadas')
 Ind_dst_xda_minutos = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_ind_dst_xda_minutos')
 Dst_xdp_llamadas = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_dst_xdp_llamadas')
 Dst_xdp_minutos = models.DecimalField(blank=True, max_digits=10, decimal_places=3,null=True,db_column='trca_dst_xdp_minutos')
 Ind_dst_xdp_llamadas = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_ind_dst_xdp_llamadas')
 Ind_dst_xdp_minutos = models.DecimalField(blank=True, max_digits=10,decimal_places=3, null=True,db_column='trca_ind_dst_xdp_minutos')
 Where_coho = models.CharField(max_length=250,  blank=True, null=True,db_column='trca_where_coho')
 Where_codi = models.CharField(max_length=250,  blank=True, null=True,db_column='trca_where_codi')
 Where_tasa = models.CharField(max_length=250,  blank=True, null=True,db_column='trca_where_tasa')
 Distinto_fonoa = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_distinto_fonoa')
 Distinto_fonob = models.DecimalField(blank=True,max_digits=10, decimal_places=3, null=True,db_column='trca_distinto_fonob')
 Ind_avg_hoy_llamadas = models.DecimalField(blank=True,max_digits=10, decimal_places=3,null=True,db_column='trca_ind_avg_hoy_llamadas')
 Ind_avg_hoy_minutos = models.DecimalField(blank=True,max_digits=10,decimal_places=3, null=True,db_column='trca_ind_avg_hoy_minutos')
 def __str__(self):
  return self.Cat_dato
 class Meta:
     managed = False
     db_table = 'tiws_risk_trafico_cab'

class RiskTraficoDet(models.Model):
  #2015-09-18 
 Proceso = models.IntegerField(primary_key=True,db_column='trde_proceso')
 Cod_riesgo = models.IntegerField(db_column='trde_cod_riesgo')
#Proceso = models.ForeignKey(RiskTraficoCab, null= True,db_column='trde_proceso',related_name='RiskTraficoDetProceso')
 Cod_riesgo = models.ForeignKey(RiskTraficoCab, db_column='trde_cod_riesgo',related_name='RiskTraficoDetCodigo')
 Tip_analisis = models.CharField(max_length=10,db_column='trde_tip_analisis')
 Cod_dato = models.CharField(max_length=20,db_column='trde_cod_dato')
 Des_dato = models.CharField(max_length=60,db_column='trde_des_dato')
 Tip_valor = models.CharField(max_length=10,db_column='trde_tip_valor')
 Fec_riesgo = models.DateField(db_column='trde_fec_riesgo')
 Dia_llamadas = models.IntegerField(blank=True, null=True,db_column='trde_dia_llamadas')
 Dia_minutos = models.BigIntegerField(blank=True, null=True,db_column='trde_dia_minutos')
 Dia_valor = models.BigIntegerField(blank=True, null=True,db_column='trde_dia_valor')
 def __str__(self):
    return self.Cat_dato
 class Meta:
    managed = False
    db_table = 'tiws_risk_trafico_det'

class consolidadoDia(models.Model):
  Fecha = models.DateField(primary_key=True,db_column='codi_fecha')
  Orig_pais = models.CharField(max_length=5, null=True,db_column='codi_orig_pais')
  Orig_area = models.CharField(max_length=10,db_column='codi_orig_area')
  Dest_pais = models.CharField(max_length=5, null=True,db_column='codi_dest_pais')
  Dest_area = models.CharField(max_length=10, blank=True, null=True,db_column='codi_dest_area')
  Ruta_entrada = models.CharField(max_length=10, blank=True, null=True,db_column='codi_ruta_entrada')
  Ruen_carrier = models.CharField(max_length=5,blank=True, null=True,db_column='codi_ruen_carrier')
  Ruen_pais = models.CharField( max_length=5,blank=True, null=True,db_column='codi_ruen_pais')
  Ruen_servicio = models.CharField(max_length=10,db_column='codi_ruen_servicio')
  Ruta_salida = models.CharField( max_length=10,blank=True, null=True,db_column='codi_ruta_salida')
  Rusa_carrier = models.CharField( max_length=5,blank=True, null=True,db_column='codi_rusa_carrier')
  Rusa_pais = models.CharField(max_length=5,blank=True, null=True,db_column='codi_rusa_pais')
  Rusa_servicio = models.CharField(max_length=10,blank=True,db_column='codi_rusa_servicio')
  Suma_llamadas = models.BigIntegerField(blank=True, null=True,db_column='codi_suma_llamadas')
  Suma_segundos = models.BigIntegerField (blank=True, null=True,db_column='codi_suma_segundos')
  Clave = models.CharField(max_length=50,blank=True,db_column='codi_clave')
  Suma_minutos = models.BigIntegerField(blank=True, null=True,db_column='codi_suma_minutos')
  def __str__(self):
    return self.Orig_pais
  class Meta:
       managed = False
       db_table = 'tiws_consolidado_dia'


