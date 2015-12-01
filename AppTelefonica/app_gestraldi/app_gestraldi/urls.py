from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.home.urls', namespace="home_app")),
    url(r'^fraude/', include('apps.fraude.urls', namespace="fraude_app")),
]
