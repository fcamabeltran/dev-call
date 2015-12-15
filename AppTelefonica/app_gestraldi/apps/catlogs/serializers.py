from rest_framework import serializers
from .models import RiskCatalogo


class RiskCatalogoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RiskCatalogo
        fields=('Codigo','Descripcion','Largo','Nivel','Estado','Funcion','Tipo_funcion')
