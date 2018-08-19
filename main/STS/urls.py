from django.conf.urls import url
from django.contrib import admin

from main.STS import views



urlpatterns = [
    # url(r'^landing/$', views.landing, name='landing'),
    # url(r'^landing/(?:(?P<sort_id>\d+)/(?P<part_id>\d+)/)?$', views.landing, name='landing'),
    url(r'^smart-toner-system/about$', views.about, name='sts_about'),
    url(r'^smart-toner-system/vopros-otvet$', views.sts_vo, name='sts_vopros-otvet'),
    url(r'^smart-toner-system/how-it-works$', views.sts_howitworks, name='sts_how-it-works'),
    url(r'^smart-toner-system/supply$', views.sts_supply, name='sts_supply'),
    url(r'^smart-toner-system/price$', views.sts_price, name='sts_price'),
    # url(r'^landing/modal/$', views.open_modal, name='openmodal')
    # url(r'^landing/(?:(?P<sort_id>\d+)/)?check/$', views.check_device, name='check'),


]
# /(?P<inform>\d)*