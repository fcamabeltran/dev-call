from django.conf.urls import url,include,patterns
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import *
#hoas
mantenimiento_urls = patterns('',

#    url(r'^fraudePais/$', PaisesList.as_view()),
#    url(r'^fraudePais/(?P<pk>[0-9a-zA-Z_-]+)/$', PaisesDetail.as_view()),
#    url(r'^fraudeServicios/$', ServiciosList.as_view()), 
#    url(r'^fraudeServicios/(?P<pk>\d+)/$', ServiciosDetail.as_view()),
#    url(r'^fraudeCentral/$', CentralList.as_view()),
#    url(r'^fraudeCentral/(?P<slug>[a-zA-Z0-9_.-]+)/$', CentralDetail.as_view()),
#    url(r'^fraudeRuta/$', RutaList.as_view()),
#    url(r'^fraudeRuta/(?P<pk>\w+)/$', RutaDetail.as_view()),
#    url(r'^fraudeServiciosEspeciales/$', ServiciosEspecialesList.as_view()),
#    url(r'^fraudeServiciosEspeciales/(?P<pk>\d+)/$', ServiciosEspecialesDetail.as_view()),
#    url(r'^paises/$', 'apps.fraude.views.crud_paises',name="paises"),
#    url(r'^servicios/$', 'apps.fraude.views.crud_servicios',name="servicios"),
#    url(r'^central/$', 'apps.fraude.views.crud_central',name="central"),
#    url(r'^ruta/$', 'apps.fraude.views.crud_ruta',name="ruta"),
#    url(r'^serviciosEspeciales/$', 'apps.fraude.views.crud_serviciosEspeciales',name="serviciosEspeciales"),
#    url(r'^addPais/$', 'apps.fraude.views.crud_addPais',name="addPais"),
#    url(r'^updatePais/$', 'apps.fraude.views.crud_updatePais',name="updatePais"),

)

diarios_urls = patterns('',
#    url(r'^riskhoy/$', RiskRatiosHoyList.as_view()),
#    url(r'^riskhoy/(?P<pk>\d+)/$', RiskRatiosHoyDetail.as_view()),
#    url(r'^riskcab/$', RiskTraficoCabList.as_view()),
#    url(r'^riskcab/(?P<pk>\d+)/$', RiskTraficoCabDetail.as_view()),
#    url(r'^riskdet/$', RiskTraficoDetList.as_view()),
#    url(r'^riskdet/(?P<pk>\d+)/$', RiskTraficoDetDetail.as_view()),
#    url(r'^riskumb/$', RiskUmbralesList.as_view()),
#    url(r'^riskumb/(?P<pk>\d+)/$', RiskUmbralesDetail.as_view()),
#    url(r'^riskcat/$', RiskCatalogoList.as_view()),
#    url(r'^riskcat/(?P<pk>\d+)/$', RiskCatalogoDetail.as_view()),
#    url(r'^tasacion/$', TasacionSolohoyList.as_view()),

    #url(r"^tasacion/(?P<cliente>[^/]+)/numerodestino/(?P<pagina>[^/]+)/$",  TasacionSolohoyList.as_view()),
) 
control_urls = patterns('',
#    url(r'^carga/$', ControlCargaList.as_view()),
#    url(r'^carga/(?P<pk>\d+)/$', ControlCargaDetail.as_view()),
)

rechazos_urls = patterns('',
#    url(r'^rechazos/$', 'apps.fraude.views.panel_rechazos',name="rechazos"),
)

produccion_urls = patterns('',
#    url(r'^respaldo/$', 'apps.fraude.views.panel_backups',name="respaldo"),
#    url(r'^reporteTrafico/$', 'apps.fraude.views.panel_reportesTrafico',name="reporteTrafico"),
#    url(r'^reporteTraficoComercial/$', 'apps.fraude.views.panel_reportesTraficoComercial',name="reportTraficComercial"),
)


modulosExternos_urls = patterns('',
#    url(r'^fraude/$', 'apps.fraude.views.panel_gestFraude',name="fraude"),
#    url(r'^salientes/$', 'apps.fraude.views.panel_salientes',name="salientes"),
)

extra_urls = patterns('',
    #url(r'^datosPersonales/$', 'apps.fraude.views.panel_datosPersonales',name="datosPersonales"),
)

reportes_urls = patterns('',
#    url(r'^analizador/$', 'apps.fraude.views.repor_analizador',name="analizador"),
#    url(r'^telefonoOrigenDestino/$', 'apps.fraude.views.repor_telefOrigenDestino',name="telefonoOrigenDestino"),
#    url(r'^detalleLlamadas/$', 'apps.fraude.views.report_detalleLlamadas',name="detalleLlamadas"),
#    url(r'^traficoAnomalo/$', 'apps.fraude.views.report_traficoAnomalo',name="traficoAnomalo"),
#    url(r'^vistaComercial/$', 'apps.fraude.views.report_vistaComercial',name="vistaComercial"),
)
 
 #demografico
urlpatterns = patterns('',
    url(r'^mantenimiento/', include(mantenimiento_urls)),
    url(r'^produc/', include(produccion_urls)),
    url(r'^', include(rechazos_urls)),
    url(r'^otros/', include(extra_urls)),
    url(r'^home/$', 'apps.fraude.views.home',name="home"),
    url(r'^report/', include(reportes_urls)),
    url(r'^diario/', include(diarios_urls)),
     url(r'^control/', include(control_urls)),
)




urlpatterns = format_suffix_patterns(urlpatterns)
