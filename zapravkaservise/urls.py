from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

if settings.DEV_MODE == True  and settings.DEBUG == True:
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.mainpage.urls')),
    url(r'^', include('main.main_content.urls')),
    url(r'^', include('main.remont_page.urls')),
    url(r'^', include('main.devices.urls')),
    url(r'^', include('main.kartridji_zapravka.urls')),
    url(r'^', include('main.STS.urls')),
    url(r'^', include('main.skup.urls')),
]
if settings.DEV_MODE == True and settings.DEBUG == True:
	urlpatterns += staticfiles_urlpatterns()
else:
	urllpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)






