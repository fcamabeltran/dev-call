from rest_framework import serializers
from .models import TasacionSolohoy,RiskRatiosHoy

class TasacionSolohoySerializer (serializers.ModelSerializer):
  Nude_ciudada     = serializers.CharField(source="Nude_ciudad.Descripcion")
  Nude_operadora = serializers.CharField(source="Nude_operador.Descripcion")
  Nude_paisa    = serializers.CharField(source="Nude_pais.Descripcion")
  Nuor_ciudada     = serializers.CharField(source="Nuor_ciudad.Descripcion")
  Nuor_operadora = serializers.CharField(source="Nuor_operador.Descripcion")
  Nuor_paisa    = serializers.CharField(source="Nuor_pais.Descripcion")
  Rutasalidaa    = serializers.CharField(source="Rutasalida.Descripcion")
  Rutaentradaa    = serializers.CharField(source="Rutaentrada.Descripcion")
  class Meta:
    model = TasacionSolohoy
    fields = ('Secuenciaproceso','Secuenciaregistro','Secuenciareproceso','Fechahora','Numeroorigen','Nuor_ciudada','Nuor_paisa','Nuor_operadora','Nuor_servicio','Numerodestino','Nude_ciudada','Nude_operadora','Nude_paisa','Nude_servicio','Numerossee','Rutaentradaa','Ruen_operador','ruen_pais','Ruen_servicio','Rutasalidaa','Rusa_operador','Rusa_pais','Rusa_servicio','Prefijo','Segundos','Modalidad','Seor_serie','Seor_operador','Seor_servicio','Seor_ciudad','Sede_serie','Sede_operador','Sede_servicio','Sede_ciudad','Sse_flag','Fuente','Flagcruce','Observacion','Match_fecha','Match_hora','Match_xxxx')

class RiskRatiosHoySerializer(serializers.HyperlinkedModelSerializer):
  Cod_dato_descripcion = serializers.CharField(source="Cod_dato.Descripcion")
  class Meta:
    model = RiskRatiosHoy
    fields=('Cod_Riesgo', 'Cod_dato_descripcion', 'Fec_riesgo', 'Cat_dato', 'Dia_llamadas', 'Dia_minutos', 'Ind_umb_llamadas', 'Ind_umb_minutos', 'Aye_llamadas', 'Aye_minutos', 'Ind_aye_llamadas', 'Ind_aye_minutos', 'Avg_xda_llamadas', 'Avg_xda_minutos', 'Ind_avg_xda_llamadas', 'Ind_avg_xda_minutos','Avg_xdp_llamadas', 'Avg_xdp_minutos', 'Ind_avg_xdp_llamadas', 'Ind_avg_xdp_minutos', 'Dst_xda_llamadas', 'Dst_xda_minutos', 'Ind_dst_xda_llamadas', 'Ind_dst_xda_minutos', 'Dst_xdp_llamadas', 'Dst_xdp_minutos', 'Ind_dst_xdp_llamadas', 'Ind_dst_xdp_minutos', 'Where_coho', 'Where_codi', 'Where_tasa')
