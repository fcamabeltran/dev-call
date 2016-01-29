from class_based_auth_views.views import LogoutView
from django.conf.urls import url
from .views import MyLoginView, UserAPI, IndexView

urlpatterns = [
    url(r'^login/$', MyLoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/me/$', UserAPI.as_view(), name='api_me'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^otros/gestraldi/$', 'apps.home.views.panelGestraldi',name="panel-gestraldi"),
   	url(r'^otros/documentos/$', 'apps.home.views.panelDocumentos',name="panel-documentos"),
]

