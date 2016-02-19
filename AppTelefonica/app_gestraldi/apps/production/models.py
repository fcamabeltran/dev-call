from django.db import models
from django.core.validators import RegexValidator

#***************************************************************************************
# MODELS: PRODUCTION
#    Ver        Date            Author          Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015          F.CB          1.-Create Models 
#**************************************************************************************/

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
    Descripcion  =models.CharField(max_length=30,null=True,db_column='pais_descripcion', validators=[
      RegexValidator(
            regex= '^[a-zA-z]*$',
            message='Este campo no debe contener numeros'
        )])
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

class DestinoRiesgo(models.Model):
  Codigo = models.IntegerField(primary_key=True,db_column='drsk_codigo')
  Descripcion  = models.CharField(max_length=30,blank = True,db_column='drsk_descripcion')
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
