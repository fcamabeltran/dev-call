from apps.control.models import controlProceso,Rechazos
from apps.control.serializers import ControlCargaSerializer,RechazosSerializer
from django.db.models import Count
from rest_framework import generics
from datetime import datetime, timedelta, time


today= datetime.now().date().isoformat()

class ControlCargaList(generics.ListCreateAPIView):
	model =  controlProceso
	queryset =  controlProceso.objects.all()
	serializer_class =  ControlCargaSerializer

class ControlCargaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = controlProceso
    queryset = controlProceso.objects.all()
    serializer_class = ControlCargaSerializer

class ControlCargaDetalle(generics.ListAPIView):
	model = controlProceso
	serializer_class = ControlCargaSerializer
	def get_queryset(self,  **kwargs):
		p_fecini=datetime.strptime(self.kwargs.get("p_fecini"), '%Y-%m-%d').date
		p_fecfin=datetime.strptime(self.kwargs.get("p_fecfin"), '%Y-%m-%d').date
		return controlProceso.objects.filter(Priregfecha__range(p_fecini,p_fecfin))

class ControlRechazosDetalle(generics.ListCreateAPIView):
	model = Rechazos
	serializer_class = RechazosSerializer
	queryset =  Rechazos.objects.all()

###### MODULO RECHAZO #######
class ControlRechazoxTipo(generics.ListAPIView):
	model=Rechazos
	serializer_class=RechazosSerializer
	def get_queryset(self, **kwargs):
		p_fecini=datetime.strptime(self.kwargs.get("p_fecini"), '%Y-%m-%d').date
		p_fecfin=datetime.strptime(self.kwargs.get("p_fecfin"), '%Y-%m-%d').date
		return Rechazos.objects.all()

class ControlRechazoxDetalle(generics.ListAPIView):
	model=Rechazos
	serializer_class=RechazosSerializer
	def get_queryset(self,**kwargs):
		p_fecini=datetime.strptime(self.kwargs.get("p_fecini"), '%Y-%m-%d')
		p_fecfin=datetime.strptime(self.kwargs.get("p_fecfin"), '%Y-%m-%d')
		error=self.kwargs.get("error")
		return Rechazos.objects.all().values('codigo','error_Descripcion',).agregate(sum('rech_segundos')/60)

class ControlRechazoxDetallexError(generics.ListAPIView):
	model=Rechazos
	serializer_class=RechazosSerializer
	def get_queryset(self):		
		error=self.kwargs.get("error") 
		return Rechazos.objects.all()



#class ListConditionalDate(generics.ListAPIView):
#    def get_serializer_class(self):
#        return DetailTodaySerializer                if not self.request.query_params.get("since")          else HistoryDetailSerializer
# 
#    def get_queryset(self):
#        return DetailModel.objects.filter(...)         if not self.request.query_params.get("since")         else HistoryModel.objects.filter()#
#

#class ListaCondition(generics.ListAPIView):
#	def get_serializer_class(self):+
#		return DetailTodaySerializer#

#	def get_queryset(self):
#		return DetailModelSerializer 