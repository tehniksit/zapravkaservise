from django.conf.urls import url
from django.contrib import admin

from main.remont_page import views

admin.autodiscover()

urlpatterns = [
    url(r'^remont$', views.remont_page, name='remont_page'),

]
