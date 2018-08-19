from django.conf.urls import url
from django.contrib import admin

from main.skup import views



urlpatterns = [
    url(r'^zakup$', views.zakup, name='zakup'),
    url(r'^zakup-hp-price$', views.zakup_hp, name='zakup-price-hp'),
    url(r'^zakup-brother-price$', views.zakup_brother, name='zakup-price-brother'),
    url(r'^zakup-kyocera-price$', views.zakup_kyocera, name='zakup-price-kyocera'),
    url(r'^zakup-canon-price$', views.zakup_canon, name='zakup-price-canon'),
    url(r'^zakup-samsung-price$', views.zakup_samsung, name='zakup-price-samsung'),


]
