from django.conf.urls import url,include,patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

today_urls = patterns('',
    url(r'^analizadorOnline/$', analizadorHoyList.as_view()),
    url(r'^analizadorOnline/(?P<pk>\d+)/$', analizadorHoyDetail.as_view()),
    url(r'^tasacion/$', TasacionSolohoyList.as_view()),

 )
urlpatterns = patterns('',
    url(r'^', include(today_urls)),
)
urlpatterns = format_suffix_patterns(urlpatterns)
