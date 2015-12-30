from .models import controlProceso
from .serializers import ControlCargaSerializer
from rest_framework import generics


# Create your views here.
class ControlCargaList(generics.ListCreateAPIView):
      model =  controlProceso
      queryset =  controlProceso.objects.all()
      serializer_class =  ControlCargaSerializer

class ControlCargaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = controlProceso
    queryset = controlProceso.objects.all()
    serializer_class = ControlCargaSerializer