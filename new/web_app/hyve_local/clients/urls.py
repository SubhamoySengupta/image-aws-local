from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.d),
    url(r'^hyve-local-resize/$', views.show),
    url(r'^hyve-local-sync/$', views.d),
    url(r'^hyve-local-resize/check/$', views.check),
]
