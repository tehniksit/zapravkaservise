from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.mainpage.urls')),
    url(r'^', include('main.main_content.urls')),
    url(r'^', include('main.remont_page.urls')),
    url(r'^', include('main.devices.urls')),
    url(r'^', include('main.kartridji_zapravka.urls')),
]
