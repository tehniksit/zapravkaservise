from django.conf.urls import url
from django.contrib import admin

from main.kartridji_zapravka import views

admin.autodiscover()

urlpatterns = [

    url(r'^zapravka/$', views.poisk_kartridj, name='poisk_kartridj'),
    url(r'^zapravka/result/?', views.result_of_poisk, name='result_of_poisk'),
    url(r'^zapravka/detail_of_cartridge/?', views.zapravka, name='detail_of_cartridge'),

]
