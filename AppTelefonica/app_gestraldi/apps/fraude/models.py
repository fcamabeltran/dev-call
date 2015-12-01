#encoding:utf-8
#***************************************************************************************
# MODELS: CATALOGOS
#    Ver        Date            Author          Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015          F.CB          1.-Create Models 
#**************************************************************************************/
from django.db import models

class Central (models.Model):
    Codigo           =models.IntegerField(primary_key=True,blank=True,db_column='cent_codigo')
    Sigla            =models.CharField(max_length=6,null=True,db_column='cent_sigla')
    Descripcion      =models.CharField(max_length=20,null=True,db_column='cent_descripcion')
    Ubicacion        =models.CharField(max_length=30,null=True,db_column='cent_ubicacion')
    PersonaContacto  =models.CharField(max_length=20,null=True,db_column='cent_personacontacto')
    TelefonoContacto =models.CharField(max_length=18,null=True,db_column='cent_telefonocontacto')
    RutaRecepcion    =models.CharField(max_length=100,null=True,db_column='cent_rutarecepcion')
    RutaProcesado    =models.CharField(max_length=100,null=True,db_column='cent_rutaprocesado')
    RutaBackup       =models.CharField(max_length=100,null=True,db_column='cent_rutabackup')
    Prefijo          =models.CharField(max_length=20,null=True,db_column='cent_prefijo')
    Sufijo           =models.CharField(max_length=20,null=True,db_column='cent_sufijo')
    SecuenciaInicial    =models.IntegerField(null=True,db_column='cent_inisecuencia')
    SecuenciaFinal     =models.IntegerField(null=True,db_column='cent_finsecuencia')
    CreacionUsuario      =models.IntegerField(null=True,db_column='cent_usrcreacion')
    FechaCreacion      =models.DateField(null=True,db_column='cent_feccreacion')
    ModificaUsr      =models.IntegerField(null=True,db_column='cent_usrmodifica')
    FechaModifica      =models.DateField(null=True,db_column='cent_fecmodifica')
    Estado           =models.CharField(max_length=1,default='A',db_column='cent_estado')
    GrupoCentral     =models.CharField(max_length=20,blank=True,null=True,db_column='cent_grupocentral')  
    def __str__(self):
      return self.Descripcion 
    class Meta:
      managed = False
      db_table = 'TIWS_CENTRAL'

class Servicio(models.Model):
    Codigo = models.CharField(primary_key=True, max_length=5,blank=False,db_column='serv_codigo')
    Descripcion = models.CharField(max_length=50,db_column='serv_descripcion')
    Sigla = models.CharField(max_length=5,db_column='serv_sigla')
    def __str__(self):
      return self.Descripcion
    class Meta:
      managed = False
      db_table = 'TIWS_SERVICIO'

class Paises(models.Model):
    Codigo       =models.CharField(primary_key=True, max_length=5, blank=False,db_column='pais_codigo')
    Descripcion  =models.CharField(max_length=30,null=True,db_column='pais_descripcion')
    Imagen       =models.ImageField(upload_to='archivos/',db_column='pais_imagen')
    Discado      =models.CharField(max_length=10,null=True,db_column='pais_discado')
    Observacion  =models.CharField(max_length=60,null=True,db_column='pais_observacion')
    Flg          =models. BooleanField(db_column='pais_flg_tiws', default='0') 
    CodigoChart  =models.CharField(max_length=2,db_column='pais_cod_chart')
    def __str__(self):
       return self.Descripcion  
    class Meta:
       managed = False
       db_table = 'TIWS_PAIS'

class PaisesPrueba(models.Model):
    Codigo       =models.CharField(primary_key=True, max_length=5, blank=False,db_column='pais_codigo')
    Descripcion  =models.CharField(max_length=30,null=True,db_column='pais_descripcion')
    Imagen       =models.ImageField(upload_to='archivos/',db_column='pais_imagen')
    Discado      =models.CharField(max_length=10,null=True,db_column='pais_discado')
    Observacion  =models.CharField(max_length=60,null=True,db_column='pais_observacion')
    Flg          =models. BooleanField(db_column='pais_flg_tiws', default='0') 
    Proceso = models.IntegerField(primary_key=True,db_column='trca_proceso')
    Cod_riesgo = models.IntegerField(db_column='trca_cod_riesgo')
    Cod_dato = models.IntegerField(db_column='trca_cod_dato')
    Fec_riesgo = models.DateField(blank=True, null=True,db_column='trca_fec_riesgo')
    Cat_dato = models.CharField(max_length=6,db_column='trca_cat_dato')
    Dia_llamadas = models.IntegerField(blank=True, null=True,db_column='trca_dia_llamadas')
    Dia_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_dia_minutos')
    Ind_umb_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_umb_llamadas')
    Ind_umb_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_umb_minutos')
    Aye_llamadas = models.IntegerField(blank=True, null=True,db_column='trca_aye_llamadas')
    Aye_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_aye_minutos')
    Ind_aye_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_aye_llamadas')
    Ind_aye_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_aye_minutos')
    Avg_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_avg_xda_llamadas')
    Avg_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_avg_xda_minutos')
    Ind_avg_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_avg_xda_llamadas')
    Ind_avg_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_avg_xda_minutos')
    Avg_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_avg_xdp_llamadas')
    Avg_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_avg_xdp_minutos')
    Ind_avg_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_avg_xdp_llamadas')
    Ind_avg_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_avg_xdp_minutos')
    Dst_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_dst_xda_llamadas')
    Dst_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_dst_xda_minutos')
    Ind_dst_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_dst_xda_llamadas')
    Ind_dst_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_dst_xda_minutos')
    Dst_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_dst_xdp_llamadas')
    Dst_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_dst_xdp_minutos')
    Ind_dst_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_dst_xdp_llamadas')
    Ind_dst_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='trca_ind_dst_xdp_minutos')
    Where_coho = models.CharField(max_length=200, blank=True, null=True,db_column='trca_where_coho')
    Where_codi = models.CharField(max_length=200, blank=True, null=True,db_column='trca_where_codi')
    Where_tasa = models.CharField(max_length=200, blank=True, null=True,db_column='trca_where_tasa')
    Distinto_fonoa = models.CharField(max_length=200,blank=True, null=True,db_column='trca_distinto_fonoa')
    Distinto_fonob = models.CharField(max_length=200,blank=True, null=True,db_column='trca_distinto_fonob')
    Ind_avg_hoy_llamadas = models.CharField(max_length=200,blank=True, null=True,db_column='trca_ind_avg_hoy_llamadas')
    Ind_avg_hoy_minutos = models.CharField(max_length=200,blank=True, null=True,db_column='trca_ind_avg_hoy_minutos')
    def __str__(self):
       return self.Descripcion  
    class Meta:
       managed = False
       db_table = 'TIWS_PAIS_PRUEBA'

class Carrier (models.Model):
    Codigo       = models.CharField(primary_key=True, max_length=5,blank=False,db_column='carr_codigo')
    Descripcion  = models.CharField(max_length=50,db_column='carr_descripcion')
    Pais = models.ForeignKey('Paises', null=True,db_column='carr_pais')
    Observacion = models.CharField(max_length=60,db_column='carr_observacion')
    def __str__(self):
      return self.Descripcion
    class Meta:
       managed = False
       db_table = 'TIWS_CARRIER'

class Indicadores(models.Model):
   Codigo = models.IntegerField(primary_key=True,db_column='cind_codigo')
   Sigla = models.CharField(max_length=10, blank=True, null=True,db_column='cind_sigla')
   Descripcion = models.CharField(max_length=50,db_column='cind_descripcion')
   Umbrales = models.BigIntegerField(blank=True, null=True,db_column='cind_umbrales')
   Estado = models.NullBooleanField(db_column='clis_estado')
   def __str__(self):
     return self.Descripcion 
   class Meta:
     managed = False
     db_table = 'TIWS_CAB_INDICADORES'

class Destino(models.Model):
   Codigo       = models.CharField(max_length=10,primary_key=True,db_column='dest_codigo')
   Descripcion  = models.CharField(max_length=50,db_column='dest_descripcion')
   Pais         = models.CharField(max_length=5,db_column='dest_pais')
   Observacion  = models.CharField(max_length=50,blank=True, null=True,db_column='dest_observacion')    
   def __str__(self):
     return self.Descripcion 
   class Meta:
     managed = False
     db_table = 'TIWS_DESTINOS'

class DetalleListas(models.Model):
   Codigo       = models.IntegerField(primary_key=True,db_column='dlis_codigo')
   Dato  = models.CharField(primary_key=True,max_length=50,db_column='dlis_dato_codigo')
   Descripcion         = models.CharField(max_length=50,db_column='dlis_dato_descripcion')
   Estado = models.NullBooleanField(db_column='dlis_estado')
   def __str__(self):
     return self.Dato 
   class Meta:
     managed = False
     db_table = 'TIWS_DET_LISTAS'

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

class Errores(models.Model):
    Codigo = models.IntegerField(primary_key=True,db_column='erro_codigo')
    Descripcion = models.CharField(max_length=60,db_column='erro_descripcion')
    Modulo = models.CharField(max_length=30, blank=True, null=True,db_column='erro_modulo')
    Usrcreacion = models.IntegerField(blank=True, null=True,db_column='erro_usrcreacion')
    Feccreacion = models.DateField(blank=True, null=True,db_column='erro_feccreacion')
    Usrmodifica = models.IntegerField(blank=True, null=True,db_column='erro_usrmodifica')
    Fecmodifica = models.DateField(blank=True, null=True,db_column='erro_fecmodifica')
    Flgrecuperable = models.CharField(max_length=1, blank=True, null=True,db_column='erro_flgrecuperable')
    def __str__(self):
      return self.Descripcion
    class Meta:
      managed = False
      db_table = 'TIWS_ERRORES'

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

class Ruta(models.Model):
    #primary key son dos CODIGO Y FECHA DE INICIO
    Codigo      = models.CharField(primary_key=True,max_length=6,blank=False,db_column='ruta_codigo' )
    Descripcion = models.CharField(max_length=50,db_column='ruta_descripcion')
    Central        = models.ForeignKey('Central',db_column='ruta_switch',related_name='Ruta')
    TipoTrafico = models.CharField(max_length=5,db_column='ruta_tipotrafico')
    FechaInicio = models.DateField(blank=False,db_column='ruta_fechainicio')
    FechaFinal  = models.DateField(db_column='ruta_fechafinal')
    Grupo       = models.CharField(max_length=50,db_column='ruta_grupo')
    Carrier     = models.CharField(max_length=5,db_column='ruta_carrier')
    Observacion = models.CharField(max_length=60,db_column='ruta_observacion')
    def __str__(self):
        return self.Descripcion
    class Meta:      
        managed = False
        db_table = 'TIWS_RUTA'

class ServiciosEspeciales(models.Model):
    Numero      = models.CharField(primary_key=True,max_length=20,blank=False,db_column='ssee_numero' )
    Pais = models.ForeignKey('Paises',db_column='ssee_pais')
    TipoDestino      = models.CharField(max_length=10,db_column='ssee_tipodestino')
    Servicio =   models.ForeignKey('Servicio',db_column='ssee_servicio')
    Destino =models.ForeignKey('Destino',db_column='ssee_destino')
    Operador  = models.CharField(max_length=5,db_column='ssee_operador')
    FechaInicio      = models.DateField(primary_key=True,db_column='ssee_fechainicio')
    FechaFinal     = models.DateField(db_column='ssee_fechafinal')
    FechadeUso = models.DateField(db_column='ssee_fechadeuso')
    FechaLoad = models.DateField(db_column='ssee_fechaload')
    Fuente = models.CharField(max_length=50,db_column='ssee_fuente')
    Observacion = models.CharField(max_length=100,db_column='ssee_observacion')
    def __str__(self):
      return self.Numero
    class Meta:
      managed = False
      db_table = 'TIWS_SSEE'

class Respaldo(models.Model):
  Tabla = models.CharField(primary_key=True,max_length=30,db_column='bcab_tabla')
  Base = models.CharField(primary_key=True,max_length=20,db_column='bcab_base')
  Rutaoutput = models.CharField(max_length=100, blank=True, null=True,db_column='bcab_rutaoutput')
  Prefijooutput = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_prefijooutput')
  Campoclave = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_campoclave')
  Diasreten_bd = models.BigIntegerField(blank=True, null=True,db_column='bcab_diasreten_bd')
  Diasreten_fs = models.BigIntegerField(blank=True, null=True,db_column='bcab_diasreten_fs')
  Claveminimaactual = models.DateField(blank=True, null=True,db_column='bcab_claveminimaactual')
  flg_backup = models.NullBooleanField(db_column='bcab_flg_backup')
  Maxdiasbackup = models.BigIntegerField(blank=True, null=True,db_column='bcab_maxdiasbackup')
  Ultimodiabackup = models.DateField(blank=True, null=True,db_column='bcab_ultimodiabackup')
  Flg_delete = models.NullBooleanField(db_column='bcab_flg_delete')
  Maxdiasdelete = models.BigIntegerField(blank=True, null=True,db_column='bcab_maxdiasdelete')
  Ultimodiadelete = models.DateField(blank=True, null=True,db_column='bcab_ultimodiadelete')
  Procedure = models.CharField(max_length=30, blank=True, null=True,db_column='bcab_procedure')
  Flg_estado = models.NullBooleanField(db_column='bcab_flg_estado' )
  def __str__(self):
    return self.Rutaoutput 
  class Meta:
    managed = False
    db_table = 'TIWS_BACKUP_CAB'

class DestinoRiesgo(models.Model):
  Codigo = models.IntegerField(primary_key=True,db_column='drsk_codigo')
  Descripcion  = models.CharField(primary_key=True,max_length=30,db_column='drsk_descripcion')
  Largo = models.CharField(max_length=100, blank=True, null=True,db_column='drsk_largo')
  Pais = models.ForeignKey('Paises', null=True,db_column='drsk_pais' )
  Carrier = models.ForeignKey('Carrier', null=True,db_column='drsk_carrier')
  Area = models.CharField(max_length=5, null=True,db_column='drsk_area')
  Servicio = models.ForeignKey('Servicio', null=True,db_column='drsk_servicio' )
  Nivelderiesgo = models.IntegerField( null=True,db_column='drsk_nivelderiesgo')
  def __str__(self):
    return self.Descripcion 
  class Meta:
    managed = False
    db_table = 'TIWS_DESTINOSDERIESGO'


#***************************************************************************************

# MODELS: ALMACENADOS
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#**************************************************************************************/


#***************************************************************************************

# MODELS: DIARIOS
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#**************************************************************************************/

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

class RiskRatiosHoy(models.Model):
 Cod_Riesgo = models.IntegerField(primary_key=True,db_column='raho_cod_riesgo')
 Cod_dato = models.IntegerField(db_column='raho_cod_dato')
 Fec_riesgo = models.DateField(blank=True, null=True,db_column='raho_fec_riesgo')
 Cat_dato = models.CharField(max_length=6,db_column='raho_cat_dato')
 Dia_llamadas = models.IntegerField(blank=True, null=True,db_column='raho_dia_llamadas')
 Dia_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_dia_minutos')
 Ind_umb_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_umb_llamadas')
 Ind_umb_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_umb_minutos')
 Aye_llamadas = models.IntegerField(blank=True, null=True,db_column='raho_aye_llamadas')
 Aye_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_aye_minutos')
 Ind_aye_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_aye_llamadas')
 Ind_aye_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_aye_minutos')
 Avg_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_avg_xda_llamadas')
 Avg_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_avg_xda_minutos')
 Ind_avg_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_avg_xda_llamadas')
 Ind_avg_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_avg_xda_minutos')
 Avg_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_avg_xdp_llamadas')
 Avg_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_avg_xdp_minutos')
 Ind_avg_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_avg_xdp_llamadas')
 Ind_avg_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_avg_xdp_minutos')
 Dst_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_dst_xda_llamadas')
 Dst_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_dst_xda_minutos')
 Ind_dst_xda_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_dst_xda_llamadas')
 Ind_dst_xda_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_dst_xda_minutos')
 Dst_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_dst_xdp_llamadas')
 Dst_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_dst_xdp_minutos')
 Ind_dst_xdp_llamadas = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_dst_xdp_llamadas')
 Ind_dst_xdp_minutos = models.BigIntegerField(blank=True, null=True,db_column='raho_ind_dst_xdp_minutos')
 Where_coho = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_coho')
 Where_codi = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_codi')
 Where_tasa = models.CharField(max_length=250, blank=True, null=True,db_column='raho_where_tasa')
 def __str__(self):
   return self.Cat_dato
 class Meta:
     managed = False
     db_table = 'tiws_risk_ratios_hoy'



class RiskTraficoCab(models.Model):
 Proceso = models.IntegerField(primary_key=True,blank=False,db_column='trca_proceso')
 Cod_riesgo = models.IntegerField( blank=False,db_column='trca_cod_riesgo')
 Cod_dato = models.IntegerField(blank=False,db_column='trca_cod_dato')
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

class RiskUmbrales(models.Model):
 Dominio = models.IntegerField(primary_key=True,db_column='umbr_dominio')
 Nivel = models.IntegerField(db_column='umbr_nivel')
 Descripcion = models.CharField(max_length=30, blank=True, null=True,db_column='umbr_descripcion')
 Largo = models.CharField(max_length=100, blank=True, null=True,db_column='umbr_largo')
 Llamadas = models.IntegerField(blank=True, null=True,db_column='umbr_llamadas')
 Minutos = models.IntegerField(blank=True, null=True,db_column='umbr_minutos')
 Cantidad = models.IntegerField(blank=True, null=True,db_column='umbr_cantidad')
 Rangoinicio = models.BigIntegerField(blank=True, null=True,db_column='umbr_rangoinicio')
 Rangofinal = models.BigIntegerField(blank=True, null=True,db_column='umbr_rangofinal')
 Estado = models.CharField(max_length=1, blank=True, null=True,db_column='umbr_estado')
 def __str__(self):
  return self.Descripcion 
 class Meta:
     managed = False
     db_table = 'tiws_risk_umbrales'

class RiskCatalogo(models.Model):
  Codigo = models.CharField(primary_key=True, max_length=1,db_column='risk_codigo')
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
    db_table = 'tiws_risk_catalogo'

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
      db_table = 'tiws_sumbase_det_xnumrdest_hoy'

class TasacionSolohoy(models.Model):  
  Secuenciaproceso = models.BigIntegerField(primary_key=True,db_column='tasa_secuenciaproceso')
  Secuenciaregistro = models.BigIntegerField(db_column='tasa_secuenciaregistro')
  Secuenciareproceso = models.BigIntegerField(blank=True, null=True,db_column='tasa_secuenciareproceso')
  Fechahora = models.DateTimeField(db_column='tasa_fechahora')
  Numeroorigen = models.CharField(max_length=20,db_column='tasa_numeroorigen')
  Nuor_pais = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nuor_pais')
  Nuor_operador = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_nuor_operador')
  Nuor_ciudad = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_nuor_ciudad')
  Nuor_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nuor_servicio')
  Numerodestino = models.CharField(max_length=20,db_column='tasa_numerodestino')
  Nude_pais = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nude_pais')
  Nude_operador = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_nude_operador')
  Nude_ciudad = models.CharField(max_length=10, blank=True, null=True,db_column='tasa_nude_ciudad')
  Nude_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_nude_servicio')
  Numerossee = models.CharField(max_length=20, blank=True, null=True,db_column='tasa_numerossee')
  Rutaentrada = models.CharField(max_length=20,db_column='tasa_rutaentrada')
  Ruen_operador = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_operador')
  ruen_pais = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_pais')
  Ruen_servicio = models.CharField(max_length=5, blank=True, null=True,db_column='tasa_ruen_servicio')
  Rutasalida = models.CharField(max_length=20,db_column='tasa_rutasalida')
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
   


#***************************************************************************************



# MODELS: CONTROL
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#**************************************************************************************/

#asf

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
    return self.Central
  class Meta:
       managed = False
       db_table = 'tiws_controlproceso'



#as
#***************************************************************************************

# MODELS: MENSAJERIA
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#**************************************************************************************/


class Mensaje(models.Model):
   Usrdestino = models.CharField(max_length=30,db_column='mens_usrdestino')
   Asunto = models.CharField(max_length=100, blank=True, null=True,db_column='mens_asunto')
   Mensaje = models.CharField(max_length=3000, blank=True, null=True,db_column='mens_mensaje')
   Flgleido = models.CharField(max_length=1, blank=True, null=True,db_column='mens_flgleido')
   Fechor_recepcion = models.DateTimeField(db_column='mens_fechor_recepcion')
   Fechor_envio = models.DateTimeField(db_column='mens_fechor_envio')
   Fechor_lectura = models.DateTimeField(db_column='mens_fechor_lectura')
   Usrorigen = models.CharField(max_length=50,db_column='mens_usrorigen')
   Secuencial = models.BigIntegerField(primary_key=True,db_column='mens_secuencial')
   Attached = models.CharField(max_length=150, blank=True, null=True,db_column='mens_attached')
   def __str__(self):
    return self.Asunto 
   class Meta:
    managed = False
    db_table = 'TIWS_MENSAJES'

