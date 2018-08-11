from django.conf.urls import url
from django.contrib import admin

from main.remont_page import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^remont$', views.remont_page, name='remont_page'),

]
urlpatterns += staticfiles_urlpatterns()
