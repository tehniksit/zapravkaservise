#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class MainPage(models.Model):

    titl_1 = models.CharField(max_length=25, blank=True, default='', verbose_name='Заголовок 1ой колонны')
    col_1 = models.TextField(max_length=1000, blank=True, default='', verbose_name='Текст 1ой колонны')
    titl_2 = models.CharField(max_length=25, blank=True, default='',verbose_name='Заголовок 2ой колонны')
    col_2 = models.TextField(max_length=1000, blank=True, default='', verbose_name='Текст 2ой колонны')
    titl_3 = models.CharField(max_length=25, blank=True, default='', verbose_name='Заголовок 3й колонны')
    col_3 = models.TextField(max_length=1000, blank=True, default='', verbose_name='Текст 3й колонны')
    def __str__(self):
        return ('Текстовые данные главной страницы')

class TextRajony(models.Model):

    title_rajony = models.CharField(max_length=50, default='', verbose_name='Заголовок')

    text_rajony = models.TextField(max_length=2000, blank=True, default='', verbose_name='Текст')

    def __str__(self):
        return (str(self.title_rajony))