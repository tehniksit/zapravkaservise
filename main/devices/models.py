#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class DeviceCategory(models.Model):
    name_cat = models.CharField(default='', verbose_name='Имя категории', max_length=128)

    def __str__(self):
        return (str(self.name_cat))



class TypeOfWork(models.Model):
    device_category = models.ForeignKey(DeviceCategory)
    diagnostika = models.IntegerField(default=0,verbose_name='Диагностика')
    profilaktika = models.IntegerField(default=0, verbose_name='Профилактика')
    teh_obs = models.IntegerField(default=0, verbose_name='Техническое обслуживание')
    rem_0kat= models.IntegerField(default=0, verbose_name='Ремонт узла 0-й категории сложности')
    rem_1kat = models.IntegerField(default=0, verbose_name='Ремонт узла 1-й категории сложности')
    rem_2kat = models.IntegerField(default=0, verbose_name='Ремонт узла 2-й категории сложности')
    rem_3kat = models.IntegerField(default=0, verbose_name='Ремонт узла 3-й категории сложности')

    def __str__(self):
        return (str(self.device_category))


class Device(models.Model):

    category = models.ForeignKey(TypeOfWork, verbose_name='Категория')
    name_dev = models.CharField(default='', verbose_name='Наименование', max_length=128)


    def __str__(self):
        return (str(self.name_dev))

class Relations(models.Model):
    dev_model = models.OneToOneField(Device, verbose_name='Устройство', primary_key=True)
    image_printer = models.ImageField(upload_to='static/img/', blank=True, verbose_name='Изображение')
    def __str__(self):
        return (str(self.dev_model))
