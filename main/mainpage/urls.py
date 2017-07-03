from django.conf.urls import url
from django.contrib import admin

from main.mainpage import views

admin.autodiscover()

urlpatterns = [

    url(r'^mainpage/?$', views.main, name='main'),


]
