from rest_framework import serializers
from .models import controlProceso,Prefijos,Parametros,Rechazos
from apps.production.models import Errores

class ControlCargaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =controlProceso
        fields=('Central','Resecuencia','Secuncia','SecuenciaProceso','Ttfilenombre','Ttfiletotalregistros','Prisecregistro','Ultsecregistro','Priregfecha','Prireghora','Ultregfecha','Ultreghora','Proc_estado','Proc_fechorini','Proc_fechorfin','Totaltasacion','Totalrechazos','Totalnacional','Totalintentos','Error','Totaldesbordes','Totalparciales','Totalinternacional','Totalrebotes')

class ParametrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Parametros
        fields=('Dominio','Codigo','Descripcion','Cadena1','Cadena2','Cadena3','Valor1','Valor2','Valor3','Estado')


class PrefijosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Prefijos
        fields=('Prefijo','Posicion','Longitud','Rutaentrada','Rutasalida','Estado','Agregar','Reemplazar','Quitar','Tipo')


class RechazosSerializer(serializers.ModelSerializer):
    DescripcionError= serializers.CharField(source="Error.Descripcion")
    class Meta:
        model = Rechazos
        fields=('Secuenciaproceso','Secuenciaregistro','DescripcionError','Fechahora','Numeroorigen','Numerodestino','Rutaentrada','Rutasalida','Ip_entrada','Ip_salida','Segundos','Salidaparcial','Numregparcial','Error','Observacion','Id_call')


