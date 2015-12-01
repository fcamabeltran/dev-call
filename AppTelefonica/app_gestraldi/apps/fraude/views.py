from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
import datetime
from datetime import date
from django.db.models import Max
from django.contrib.auth.models import User

#from django.contrib.auth.models import User#
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_frawork.permissions import IsAuthenticated
#from rest_framework.response import Response
#from rest_framework.views import APIView
#asdfas
class TasacionSolohoyList(generics.ListCreateAPIView):
    model = TasacionSolohoy
    queryset = TasacionSolohoy.objects.order_by('Secuenciaproceso')[:10]
    serializer_class = TasacionSolohoySerializer

class PaisesList(generics.ListCreateAPIView):
    model = Paises
    #queryset = Paises.objects.all().aggregate(Max(str('Discado')))
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class PaisesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Paises
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class PaisesPruebaList(generics.ListCreateAPIView):
    model = PaisesPrueba
    queryset = PaisesPrueba.objects.all()     
    serializer_class = PaisesPruebaSerializer
 #   def list(self, request, *args, **kwargs):
#        print request.User
#        return super(PaisesPruebaList, self).list(request,*args, *kwargs)

class PaisesPruebaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PaisesPrueba
    queryset = PaisesPrueba.objects.all()
    serializer_class = PaisesPruebaSerializer


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
      #queryset = Ruta.objects.filter(Central__exact=1).select_related()
      #queryset = Ruta.objects.prefetch_related('Central_MM.set', 'Paises_set').all()
      date=date.today()
      #queryset=Paises.objects.filter(Fecha__exact= Fecha__year=today.year) ,(date__month=today.month),(date__day=today.day))
      #queryset=Paises.objects.filter(FechaFinal__exact=datetime.date.today())
      #queryset=Ruta.objects.filter(FechaFinal__exact=datetime.date.today())

      #queryset= Paises.objects.raw('select * from tiws_ruta')


      print(date)
     #queryset = Ruta.objects.filter(Fec_riesgo__gte=datetime(date__year=today.year, date__month=today.month, date__day=today.day))
      #queryset =Ruta.objects.filter(Central__pk=1).select_related()
     #queryset = Ruta.objects.filter(FechaInicio__gte=datetime(date__year=today.year, date__month=today.month, date__day=today.day))
     #queryset =  Ruta.objects.filter(Central__in=Central.objects.values_list('Codigo'))
      
      ##Argument.objects.all().aggregate(Max('rating'))

      ##All_Ruta = Ruta.objects.select_related('Central').all()[0: 100]
      ##for Ruta in All_Ruta:
      ##print(All_Ruta)
      ##queryset = All_Ruta

       #Client.objects.filter(id__in=Accion.objects.values_list('id', flat=True)).values('nombre', 'cantidad')
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

        
#***************************************************************************************
# VIEWS: CONTROL
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate views
# 
#**************************************************************************************/
class ControlCargaList(generics.ListCreateAPIView):
      model =  controlProceso
      queryset =  controlProceso.objects.all()
      serializer_class =  ControlCargaSerializer

class ControlCargaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = controlProceso
    queryset = controlProceso.objects.all()
    serializer_class = ControlCargaSerializer

#***************************************************************************************
# VIEWS: DIARIOS
#    Ver        Date            Author    Description
# ---------     --------        ----------       -------------
#   1.0       10/07/2015      Developer01     1.-Modificate views
# 
#**************************************************************************************/

#class AnomaliasList(generics.ListAPIView):
#    model = Anomalias
#    queryset = Anomalias.objects.all()
#    serializer_class = PaisesSerializer

class RiskRatiosHoyList(generics.ListCreateAPIView):
    model = RiskRatiosHoy
    queryset = RiskRatiosHoy.objects.all()
    serializer_class = RiskRatiosHoySerializer

class RiskRatiosHoyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskRatiosHoy
    queryset = RiskRatiosHoy.objects.all()
    serializer_class = RiskRatiosHoySerializer



class RiskTraficoCabList(generics.ListAPIView):
    model = RiskTraficoCab


#--    #max_ =  RiskTraficoCab.objects.filter(Fec_riesgo__exact=datetime.date.today())
#--#    max_ =  RiskTraficoCab.objects.filter(Fec_riesgo__exact=datetime.datetime.now().date()) 
#--#    op = max_.aggregate(Max('Proceso'))
#-- #   print(max_)
#-- #   print(op)
#--    queryset = op
      #queryset=Paises.objects.filter(FechaFinal__exact=datetime.date.today())

    #datetime(2005, 1, 30)


    #queryset=RiskTraficoCab.objects.values('Proceso','Cod_dato','Dia_llamadas','Dia_minutos','Ind_aye_minutos','Ind_avg_xda_minutos','Ind_avg_xdp_minutos','Dia_minutos','Ind_avg_hoy_minutos')
    queryset = RiskTraficoCab.objects.all()
    serializer_class = RiskTraficoCabSerializer
class RiskTraficoCabDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskTraficoCab
    queryset = RiskTraficoCab.objects.all()
    serializer_class = RiskTraficoCabSerializer

class RiskTraficoDetList(generics.ListAPIView):
    model = RiskTraficoDet
    queryset = RiskTraficoDet.objects.all()
    serializer_class = RiskTraficoDetSerializer

class RiskTraficoDetDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskTraficoDet
    queryset = RiskTraficoDet.objects.all()
    serializer_class = RiskTraficoDetSerializer
  
class RiskUmbralesList(generics.ListAPIView):
    model = RiskUmbrales
    queryset = RiskUmbrales.objects.all()
    serializer_class = RiskUmbralesSerializer

class RiskUmbralesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskUmbrales
    queryset = RiskUmbrales.objects.all()
    serializer_class = RiskUmbralesSerializer

class RiskCatalogoList(generics.ListAPIView):
    model = RiskCatalogo
    queryset = RiskCatalogo.objects.all()
    serializer_class = RiskCatalogoSerializer

class RiskCatalogoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RiskCatalogo
    queryset = RiskCatalogo.objects.all()
    serializer_class = RiskCatalogoSerializer
      
def homeFraude(request):
    return render(frequest,'base.html')
 
def home(request):
    return render(request,'produccion/produccion.html')

#MANTENIMIENTOS DE TABLAS

def crud_paises(request):
    return render(request,'mantenimientos/paises.html')


def crud_servicios(request):
    return render(request,'mantenimientos/servicios.html')

def crud_ruta(request):
    return render(request,'mantenimientos/ruta.html')

def crud_serviciosEspeciales(request):
    return render(request,'mantenimientos/serviciosEspeciales.html')

def crud_central(request):
    return render(request,'mantenimientos/central.html')

#**********************COMPONENTES*******************************
#RECHAZOS
def panel_rechazos(request):
    return render(request,'rechazos/analisisRechazo.html')

#PRODUCCIÓN
def panel_backups(request):
    return render(request,'produccion/backups.html')

def panel_reportesTrafico(request):
    return render(request,'produccion/reportesTrafico.html')

def panel_reportesTraficoComercial(request):
    return render(request,'produccion/reportesTrafico.html')
#MODULOSEXTERNOS
def panel_gestFraude(request):
    return render(request,'modulosExternos/gestFraude.html')

def panel_salientes(request):
    return render(request,'modulosExternos/salientes.html')

# USUARIOS
def panel_datosPersonales(request):
    return render(request,'extra/datosPersonales.html')

def panel_contrasenia(request):
    return render(request,'extra/datosPersonales.html')

def panel_consultas(request):
    return render(request,'extra/consultas.html')
# HOME
def home(request):
    return render(request,'principal/principal.html')

#-----------------REPORTES -----------------------

def repor_analizador(request):
    return render(request,'reportes/analizador.html')

def report_detalleLlamadas(request):
    return render(request,'reportes/detalleLlamadas.html')

def repor_telefOrigenDestino(request):
    return render(request,'reportes/telefonoOrigenDestino.html')

def report_traficoAnomalo(request):
    return render(request,'reportes/traficoAnomalo.html')

def report_vistaComercial(request):
    return render(request,'reportes/vistaComercial.html')
