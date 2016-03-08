from django.conf.urls import url,include,patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

production_urls = patterns('',

    url(r'^fraudePais/?$', PaisesList.as_view()),
    url(r'^fraudePais/(?P<pk>[0-9a-zA-Z_-]+)/$', PaisesDetail.as_view()),
    #url(r'^fraudeDetalle/(\d+)/(\D+)/$', PaisDetalle.as_view()),
    url(r'^fraudeServicios/$', ServiciosDetail.as_view()), 
    url(r'^fraudeServicios/(?P<pk>\d+)/$', ServiciosDetail.as_view()),
    url(r'^fraudeCentral/$', CentralList.as_view()),
    url(r'^fraudeCentral/(?P<slug>[a-zA-Z0-9_.-]+)/$', CentralDetail.as_view()),
    url(r'^fraudeRuta/$', RutaList.as_view()),
    url(r'^fraudeRuta/(?P<pk>\w+)/$', RutaDetail.as_view()),

   url(r'^fraudeDetalle/(?P<discado>\d+)/(?P<codigo>\D+)/$', PaisDetalle.as_view()),
    url(r'^fraudeServiciosEspeciales/$', ServiciosEspecialesList.as_view()),
    url(r'^fraudeServiciosEspeciales/(?P<pk>\d+)/$', ServiciosEspecialesDetail.as_view()),

    #url(r'^riskumb/$', RiskUmbralesList.as_view()),
    url(r'^riskumb/(?P<pk>\d+)/$', RiskUmbralesDetail.as_view()),
)
urlpatterns = patterns('',
    url(r'^', include(production_urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns)
