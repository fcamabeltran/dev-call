from rest_framework import serializers
from .models import *

class PaisesSerializer(serializers.ModelSerializer): 
     class Meta:
        model = Paises
        fields = ('Codigo', 'Descripcion', 'Imagen', 'Discado', 'Observacion','Flg','CodigoChart')

class PaisesPruebaSerializer(serializers.ModelSerializer): 
     class Meta:
        model = PaisesPrueba
        fields = ('Codigo', 'Descripcion', 'Imagen', 'Discado', 'Observacion','Flg','Proceso','Cod_riesgo','Cod_dato','Fec_riesgo','Cat_dato','Dia_llamadas','Dia_minutos','Ind_umb_llamadas','Ind_umb_minutos','Aye_llamadas','Aye_minutos','Ind_aye_llamadas','Ind_aye_minutos','Avg_xda_llamadas','Avg_xda_minutos','Ind_avg_xda_llamadas','Ind_avg_xda_minutos','Avg_xdp_llamadas','Avg_xdp_minutos','Ind_avg_xdp_llamadas','Ind_avg_xdp_minutos','Dst_xda_llamadas','Dst_xda_minutos','Ind_dst_xda_llamadas','Ind_dst_xda_minutos','Dst_xdp_llamadas','Dst_xdp_minutos','Ind_dst_xdp_llamadas','Ind_dst_xdp_minutos','Where_coho','Where_codi','Where_tasa','Distinto_fonoa','Distinto_fonob','Ind_avg_hoy_llamadas','Ind_avg_hoy_minutos')

class CentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Central
        fields = ('Codigo','Sigla','Descripcion','Ubicacion','PersonaContacto','TelefonoContacto','RutaRecepcion','RutaProcesado','RutaBackup','Prefijo','Sufijo','SecuenciaInicial','SecuenciaFinal','CreacionUsuario','FechaCreacion','ModificaUsr','FechaModifica','Estado','GrupoCentral')
    
class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('Codigo','Descripcion','Sigla')

    #StringRelatedField(many=True)
    #//AQUI = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ('Codigo', 'Descripcion', 'Observacion', 'Pais')

    #Central = serializers.HyperlinkedRelatedField(read_only=True)
    #Central = serializers.StringRelatedField()
    #Central = serializers.ReadOnlyField(many=False,read_only=True)

class RutaSerializer(serializers.ModelSerializer):
    #Central = serializers.HyperlinkedRelatedField(many=True, view_name='central-detail', read_only=True)
    Central = serializers.StringRelatedField()
   # snippets=serializers.HyperlinkedModelSerializer(many=True,view_name=)
    class Meta:
        model = Ruta
        fields = ('Codigo','Central','TipoTrafico','FechaInicio','FechaFinal','Grupo','Carrier','Observacion')

class TasacionSolohoySerializer (serializers.ModelSerializer):
    class Meta:
        model = TasacionSolohoy
        fields = ('Secuenciaproceso','Secuenciaregistro','Secuenciareproceso','Fechahora','Numeroorigen','Nuor_pais','Nuor_operador','Nuor_ciudad','Nuor_servicio','Numerodestino','Nude_pais','Nude_operador','Nude_ciudad','Nude_servicio','Numerossee','Rutaentrada','Ruen_operador','ruen_pais','Ruen_servicio','Rutasalida','Rusa_operador','Rusa_pais','Rusa_servicio','Prefijo','Segundos','Modalidad','Seor_serie','Seor_operador','Seor_servicio','Seor_ciudad','Sede_serie','Sede_operador','Sede_servicio','Sede_ciudad','Sse_flag','Fuente','Flagcruce','Observacion','Match_fecha','Match_hora','Match_xxxx')

class ServiciosEspecialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosEspeciales
        fields = ('Numero', 'Pais', 'TipoDestino', 'Servicio', 'Operador','FechaInicio','FechaFinal','FechadeUso','FechaLoad','Fuente','Observacion')


#***************************************************************************************
# MODELS: DIARIOS
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#**************************************************************************************/

class RiskRatiosHoySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskRatiosHoy
        fields=('Cod_Riesgo', 'Cod_dato', 'Fec_riesgo', 'Cat_dato', 'Dia_llamadas', 'Dia_minutos', 'Ind_umb_llamadas', 'Ind_umb_minutos', 'Aye_llamadas', 'Aye_minutos', 'Ind_aye_llamadas', 'Ind_aye_minutos', 'Avg_xda_llamadas', 'Avg_xda_minutos', 'Ind_avg_xda_llamadas', 'Ind_avg_xda_minutos','Avg_xdp_llamadas', 'Avg_xdp_minutos', 'Ind_avg_xdp_llamadas', 'Ind_avg_xdp_minutos', 'Dst_xda_llamadas', 'Dst_xda_minutos', 'Ind_dst_xda_llamadas', 'Ind_dst_xda_minutos', 'Dst_xdp_llamadas', 'Dst_xdp_minutos', 'Ind_dst_xdp_llamadas', 'Ind_dst_xdp_minutos', 'Where_coho', 'Where_codi', 'Where_tasa')
    #StringRelatedField(many=True)
    #//AQUI = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
class RiskTraficoCabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RiskTraficoCab
        fields=('Proceso','Cod_dato','Fec_riesgo','Cat_dato','Dia_llamadas','Dia_minutos','Ind_umb_llamadas','Ind_umb_minutos','Aye_llamadas','Aye_minutos','Ind_aye_llamadas','Ind_aye_minutos','Avg_xda_llamadas','Avg_xda_minutos','Ind_avg_xda_llamadas','Ind_avg_xda_minutos','Avg_xdp_llamadas','Avg_xdp_minutos','Ind_avg_xdp_llamadas','Ind_avg_xdp_minutos','Dst_xda_llamadas','Dst_xda_minutos','Ind_dst_xda_llamadas','Ind_dst_xda_minutos','Dst_xdp_llamadas','Dst_xdp_minutos','Ind_dst_xdp_llamadas','Ind_dst_xdp_minutos','Where_coho','Where_codi','Where_tasa','Distinto_fonoa','Distinto_fonob','Ind_avg_hoy_llamadas','Ind_avg_hoy_minutos')

class RiskTraficoDetSerializer(serializers.HyperlinkedModelSerializer):
    #RiskTraficoCab = serializers.ManyHyperlinkedRelatedField(view_name='RiskTraficoCab-detail')
    #RiskTraficoCab  = serializers.HyperlinkedRelatedField(view_name='RiskTraficoDetCodigo-detail',source='RiskTraficoCab',blank=True,read_only=True)
    ##RiskTraficoCab = serializers.HyperlinkedRelatedField(view_name='risktraficocab-detail',queryset=RiskTraficoCab.objects.all())
    #RiskTraficoCab = serializer.ManyHyperlinkRelateadField(view_name='RiskTraficoCab-detail')       class Meta:
    model =RiskTraficoDet
    fields=('Proceso','Tip_analisis','Cod_dato','Des_dato','Tip_valor','Fec_riesgo','Dia_llamadas','Dia_minutos','Dia_valor')

class RiskUmbralesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RiskUmbrales
        fields=('Dominio','Nivel','Descripcion','Largo','Llamadas','Minutos','Cantidad','Rangoinicio','Rangofinal','Estado')

class RiskCatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RiskCatalogo
        fields=('Codigo','Descripcion','Largo','Nivel','Estado','Funcion','Tipo_funcion')

#***************************************************************************************
# MODELS: control
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate Models
# 
#********************************************************************** ****************/ç


class ControlCargaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =controlProceso
        fields=('Central','Resecuencia','Secuncia','SecuenciaProceso','Ttfilenombre','Ttfiletotalregistros','Prisecregistro','Ultsecregistro','Priregfecha','Prireghora','Ultregfecha','Ultreghora','Proc_estado','Proc_fechorini','Proc_fechorfin','Totaltasacion','Totalrechazos','Totalnacional','Totalintentos','Error','Totaldesbordes','Totalparciales','Totalinternacional','Totalrebotes')

