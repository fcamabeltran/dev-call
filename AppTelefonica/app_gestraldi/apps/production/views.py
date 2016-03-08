from .models import Paises,ServiciosEspeciales,Central,Ruta,RiskUmbrales,Servicio
from .serializers import PaisesSerializer,ServiciosEspecialesSerializer,CentralSerializer,RutaSerializer,RiskUmbralesSerializer,ServiciosSerializer
from datetime import datetime, timedelta, time
from rest_framework import generics
  
class PaisesList(generics.ListCreateAPIView):
    model = Paises
    serializer_class = PaisesSerializer
    queryset = Paises.objects.all()[:30]

class PaisesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Paises
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class PaisDetalle(generics.ListAPIView):
    model = Paises
    serializer_class=PaisesSerializer
    def get_queryset(self, **kwargs):    
        discado=self.kwargs.get("discado")
        codigo=self.kwargs.get("codigo")
        print(Paises.objects.filter(Discado__icontains=discado,Codigo__icontains=codigo))
        return Paises.objects.filter(Discado__icontains=discado,Codigo__icontains=codigo)

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

class ServicioDetalle(generics.ListAPIView):
    model =ServiciosEspeciales
    serializer_class= ServiciosEspecialesSerializer
    today= datetime.now().date().strftime("%d/%m/%y")
    today= datetime.now().date().isoformat()

    def get_queryset(self):
    	fecha = datetime.strptime(request.GET.get("fecha"), '%Y-%m-%d')
    	numero=self.request.query_params.get("numero")
    	pais=self.request.query_params.get("pais")
    	return ServiciosEspeciales.objects.filter(FechaInicio__icontains=fecha,Numero__icontains=numero,Pais__Codigo__icontains=pais)

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

