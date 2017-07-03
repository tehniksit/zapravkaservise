#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from main.devices.models import Device

class Zapravka(models.Model):
    BRAND_CHOICES = (
        ('HP', 'HP'),
        ('Canon', 'Canon'),
        ('Kyocera', 'Kyocera'),
        ('Brother', 'Brother'),
        ('Samsung', 'Samsung'),
        ('KonicaMinolta', 'KonicaMinolta'),
        ('Другой', 'Другой')
    )
    COLOR_CHOICES = (
        ('Черный' , 'Black'),
        ('Красный', 'Magenta'),
        ('Голубой' , 'Cyan'),
        ('Желтый' , 'Yellow'),
       )


    short_name = models.CharField(default='', verbose_name='Короткое название', max_length=128)
    long_name = models.CharField(default='', verbose_name='Полное название', max_length=128, null=True, blank=True)
    manufacturer = models.CharField(choices=BRAND_CHOICES, default='HP', verbose_name='Производитель', max_length=128)
    type = models.CharField(default='Тонер-картридж', verbose_name='Тип', max_length=128)
    lifespan = models.IntegerField(default=0, verbose_name='Ресурс')
    color = models.CharField(choices=COLOR_CHOICES, default='Black', verbose_name='Цвет', max_length=128)
    compatibility = models.ManyToManyField(Device, verbose_name='Совместимость', blank=True)
    price = models.IntegerField(default=0, verbose_name='Цена')
    price_2 = models.IntegerField(default=0, verbose_name='Цена от 2-х')
    price_4 = models.IntegerField(default=0, verbose_name='Цена от 4-х')
    price_5 = models.IntegerField(default=0, verbose_name='Цена от 5-х')
    image_kartridj = models.ImageField(upload_to='static/img/kartridj/', blank=True, verbose_name='Изображение')
    def __str__(self):
        return (str(self.manufacturer)+' '+ str(self.short_name)+' '+str(self.long_name)+' '+str(self.price)+' '+str(self.color))

