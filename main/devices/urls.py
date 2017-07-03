from django.conf.urls import url
from django.contrib import admin

from main.devices import views

admin.autodiscover()

urlpatterns = [
    url(r'^devices$', views.device, name='device'),
    url(r'^device/detail$', views.detail_of_printer, name='detail_of_printer'),
    url(r'^remont/brand_choose$', views.brand_choose, name='brand_choose'),
    url(r'^remont/printer_choose$', views.device, name='printer_choose'),
]
