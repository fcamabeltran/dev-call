from .models import Paises,ServiciosEspeciales,Central,Ruta,RiskUmbrales,Servicio
from .serializers import PaisesSerializer,ServiciosEspecialesSerializer,CentralSerializer,RutaSerializer,RiskUmbralesSerializer,ServiciosSerializer
from rest_framework import generics
  
class PaisesList(generics.ListCreateAPIView):
    model = Paises
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class PaisesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Paises
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class ServiciosList(generics.ListCreateAPIView):
    model = Servicio
    queryset = Servicio.objects.all()
    serializer_class = ServiciosSerializer

class ServiciosDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Servicio
    queryset = Servicio.objects.all()
    serializer_class = ServiciosSerializer


class CentralList(generics.ListCreateAPIView):
    model =  Central
    queryset =  Central.objects.all()
    serializer_class =  CentralSerializer

class CentralDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Central
    queryset = Central.objects.all()
    serializer_class = CentralSerializer

class RutaList(generics.ListCreateAPIView):
      model =  Ruta
      queryset = Ruta.objects.all()
      serializer_class =  RutaSerializer

class RutaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Ruta
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    
class ServiciosEspecialesList(generics.ListCreateAPIView):
      model =  ServiciosEspeciales
      queryset =  ServiciosEspeciales.objects.all()
      serializer_class =  ServiciosEspecialesSerializer

class ServiciosEspecialesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ServiciosEspeciales
    queryset = ServiciosEspeciales.objects.all()
    serializer_class = ServiciosEspecialesSerializer

class RiskUmbralesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskUmbrales
    queryset = RiskUmbrales.objects.all()
    serializer_class = RiskUmbralesSerializer

