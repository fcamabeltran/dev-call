from django.conf.urls import url,include,patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

control_urls = patterns('',
    url(r'^carga/?$', ControlCargaList.as_view()),
    url(r'^carga/(?P<pk>\d+)/$', ControlCargaDetail.as_view()),
   	#url(r'^qryControl/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$', ControlCargaDetalle.as_view()),
	url(r'^rechazosDetalle/?$', ControlRechazosDetalle.as_view()),
   	#url(r'^fraudeDetalle/(?P<discado>\d+)/(?P<codigo>\D+)/$', PaisDetalle.as_view()),
    #url(r'^rechazoTipo/(?P<error>\d+)/$', ControlRechazoxDetallexError.as_view()),
    url(r'^rechazoTipo/$', ControlRechazoxDetallexError.as_view()),
    
 )
urlpatterns = patterns('',
    url(r'^', include(control_urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
   
