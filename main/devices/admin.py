from django.contrib import admin
from main.devices.form import *

class DeviceSearchAdmin(admin.ModelAdmin):
    search_fields = ['name_dev',]
    list_display = ('name_dev', 'category', 'id')
    list_filter = ('category',)

class RelationsAdmin(admin.ModelAdmin):
    raw_id_fields = ("dev_model",)
    search_fields = ['dev_model', ]
    list_display = ('get_name','get_categ',)

    def get_name(self, obj):
        return obj.dev_model.name_dev

    def get_categ(self, obj):
        return obj.dev_model.category

    get_name.short_description = 'Наименование'
    get_categ.short_description = 'Категория'

admin.site.register(Device, DeviceSearchAdmin)
admin.site.register(TypeOfWork)
admin.site.register(DeviceCategory)
admin.site.register(Relations, RelationsAdmin)