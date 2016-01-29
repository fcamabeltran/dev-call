from .models import RiskTraficoCab
from .serializers import RiskTraficoCabSerializer
from rest_framework import generics
 
class traficoList(generics.ListCreateAPIView):
	model = RiskTraficoCab
	queryset = RiskTraficoCab.objects.all()
	serializer_class = RiskTraficoCabSerializer

