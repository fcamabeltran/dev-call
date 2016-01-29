from rest_framework import serializers
from .models import Central,Servicio,Paises,Carrier,Destino,Ruta,ServiciosEspeciales,DestinoRiesgo,RiskUmbrales


class CentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Central
        fields = ('Codigo','Sigla','Descripcion','Ubicacion','PersonaContacto','TelefonoContacto','RutaRecepcion','RutaProcesado','RutaBackup','Prefijo','Sufijo','SecuenciaInicial','SecuenciaFinal','CreacionUsuario','FechaCreacion','ModificaUsr','FechaModifica','Estado','GrupoCentral')

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('Codigo','Descripcion','Sigla')

class PaisesSerializer(serializers.ModelSerializer):
    Discado = serializers.SerializerMethodField()
    Codigo = serializers.SerializerMethodField() 
      
    def get_Discado(self, obj):
        return obj.Discado.strip()
 
    def get_Codigo(self, obj):
        return obj.Codigo.strip()
    class Meta:
        model = Paises
        fields = ('Codigo', 'Descripcion', 'Imagen', 'Discado', 'Observacion','Flg','CodigoChart')


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ('Codigo', 'Descripcion', 'Observacion', 'Pais')

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ('Codigo',   'Descripcion',   'Pais',   'Observacion')


class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ('Codigo','Descripcion','Central','TipoTrafico','FechaInicio','FechaFinal','Grupo','Carrier','Observacion')


class ServiciosEspecialesSerializer(serializers.ModelSerializer):
    Numero = serializers.SerializerMethodField()
 
    def get_Numero(self, obj):
        return obj.Numero.strip()
 
    class Meta:
        model = ServiciosEspeciales
        fields =  ('Numero', 'Pais', 'TipoDestino', 'Servicio', 'Destino', 'Operador', 'FechaInicio', 'FechaFinal', 'FechadeUso', 'FechaLoad', 'Fuente', 'Observacion')

class DestinoRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinoRiesgo
        fields =  ('Codigo','Descripcion','Largo','Pais','Carrier','Area','Servicio','Nivelderiesgo')

class RiskUmbralesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =RiskUmbrales
        fields=('Dominio','Nivel','Descripcion','Largo','Llamadas','Minutos','Cantidad','Rangoinicio','Rangofinal','Estado')






