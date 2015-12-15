from rest_framework import serializers
from .models import RiskTraficoCab,RiskTraficoDet
    #StringRelatedField(many=True)
    #//AQUI = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
class RiskTraficoCabSerializer(serializers.ModelSerializer):
    Cod_pais_carrier     = serializers.CharField(source="Cod_dato.Largo")
    class Meta:
        model =RiskTraficoCab
        fields=('Proceso','Fec_riesgo','Cat_dato','Cod_pais_carrier','Dia_llamadas','Dia_minutos','Ind_umb_llamadas','Ind_umb_minutos','Aye_llamadas','Aye_minutos','Ind_aye_llamadas','Ind_aye_minutos','Avg_xda_llamadas','Avg_xda_minutos','Ind_avg_xda_llamadas','Ind_avg_xda_minutos','Avg_xdp_llamadas','Avg_xdp_minutos','Ind_avg_xdp_llamadas','Ind_avg_xdp_minutos','Dst_xda_llamadas','Dst_xda_minutos','Ind_dst_xda_llamadas','Ind_dst_xda_minutos','Dst_xdp_llamadas','Dst_xdp_minutos','Ind_dst_xdp_llamadas','Ind_dst_xdp_minutos','Where_coho','Where_codi','Where_tasa','Distinto_fonoa','Distinto_fonob','Ind_avg_hoy_llamadas','Ind_avg_hoy_minutos')

class RiskTraficoDetSerializer(serializers.HyperlinkedModelSerializer):
    #RiskTraficoCab = serializers.ManyHyperlinkedRelatedField(view_name='RiskTraficoCab-detail')
    #RiskTraficoCab  = serializers.HyperlinkedRelatedField(view_name='RiskTraficoDetCodigo-detail',source='RiskTraficoCab',blank=True,read_only=True)
    ##RiskTraficoCab = serializers.HyperlinkedRelatedField(view_name='risktraficocab-detail',queryset=RiskTraficoCab.objects.all())
    #RiskTraficoCab = serializer.ManyHyperlinkRelateadField(view_name='RiskTraficoCab-detail')       class Meta:
    model =RiskTraficoDet
    fields=('Proceso','Tip_analisis','Cod_dato','Des_dato','Tip_valor','Fec_riesgo','Dia_llamadas','Dia_minutos','Dia_valor')



