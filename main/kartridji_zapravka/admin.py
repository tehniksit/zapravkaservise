from django.contrib import admin
from main.kartridji_zapravka.form import *


class ArticleAdmin(admin.ModelAdmin):

    raw_id_fields = ("compatibility",)
    list_display = ('short_name', 'price','price_v', 'lifespan', 'get_name' )
    list_filter = ('manufacturer', )
    search_fields = ['long_name', 'short_name', ]

    def get_name(self, obj):
        return ', '.join([p.name_dev for p in obj.compatibility.all()])

    get_name.short_description = 'Подходят устройства'

admin.site.register(Zapravka, ArticleAdmin )