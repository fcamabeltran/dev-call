from .models import TasacionSolohoy,RiskRatiosHoy
from apps.store.models import RiskTraficoCab
from apps.store.serializers import RiskTraficoCabSerializer
from .serializers import TasacionSolohoySerializer,RiskRatiosHoySerializer
from rest_framework import generics


class TasacionSolohoyList(generics.ListCreateAPIView):
    models = TasacionSolohoy
    serializer_class = TasacionSolohoySerializer
    def get_queryset(self):
      query = TasacionSolohoy.objects.filter().order_by('Secuenciaproceso')[:10]
      return query

class consultaLlamada(generics.ListAPIView):
    model = TasacionSolohoy
    serializer_class = TasacionSolohoySerializer
    def get_queryset(self):
      numera = self.request.query_params.get('numera')
      numerb = self.request.query_params.get('numerb')
      query = TasacionSolohoy.objects.filter(Numeroorigen=numera,Numerodestino=numerb).order_by('Secuenciaproceso')[:s] % none
      return query

class tasacionsolohoyList(generics.ListAPIView):
    model = TasacionSolohoy
    def get_queryset(self):
      query = TasacionSolohoy.objects.filter().order_by('secuenciaproceso')[:10]
      return query

class analizadorHoyList(generics.ListCreateAPIView):
    model = RiskTraficoCab
    queryset = RiskTraficoCabSerializer.objects.all()
    serializer_class = RiskRatiosHoySerializer

class analizadorHoyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskTraficoCabSerializer
    queryset = RiskTraficoCabSerializer.objects.all()
    serializer_class = RiskRatiosHoySerializer

