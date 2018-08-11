
from django.conf.urls import url
from django.contrib import admin

from main.mainpage import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    url(r'^mainpage/?$', views.main, name='main'),


]
urlpatterns += staticfiles_urlpatterns()
