from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.home.urls', namespace="home_app")),
    url(r'^fraude/', include('apps.fraude.urls', namespace="fraude_app")),
    url(r'^catlogs/', include('apps.catlogs.urls', namespace="catlogs_api")),
    url(r'^control/', include('apps.control.urls', namespace="control_api")),
    url(r'^production/', include('apps.production.urls', namespace="production_api")),
    url(r'^security/', include('apps.security.urls', namespace="secruity_api")),
    url(r'^store/', include('apps.store.urls', namespace="store_api")),
    url(r'^today', include('apps.today.urls', namespace="today_api")),
    

]
