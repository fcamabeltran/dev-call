from django.conf.urls import url,include,patterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

store_urls = patterns('',
    url(r'^traficoList/$', traficoList.as_view()),
 )

urlpatterns = patterns('',
    url(r'^', include(store_urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
