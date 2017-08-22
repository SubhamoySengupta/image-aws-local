from django.conf.urls import include, url
from django.contrib import admin
import clients.views as cl


urlpatterns = [
    url(r'^$', cl.home, name='home'),
    url(r'^cli/', include('clients.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
