from django.db import models



class HP(models.Model):

    name_kart = models.CharField(max_length=50, default='', verbose_name='Наименование')

    price_kart = models.IntegerField(default=0,verbose_name='Цена')

    def __str__(self):
        return (str(self.name_kart)+'--'+str(self.price_kart)+'руб')


class Brother(models.Model):

    name_kart = models.CharField(max_length=50, default='', verbose_name='Наименование')

    price_kart = models.IntegerField(default=0,verbose_name='Цена')

    def __str__(self):
        return (str(self.name_kart)+'--'+str(self.price_kart)+'руб')

class Kyocera(models.Model):

    name_kart = models.CharField(max_length=50, default='', verbose_name='Наименование')

    price_kart = models.IntegerField(default=0,verbose_name='Цена')

    def __str__(self):
        return (str(self.name_kart)+'--'+str(self.price_kart)+'руб')

class Canon(models.Model):

    name_kart = models.CharField(max_length=50, default='', verbose_name='Наименование')

    price_kart = models.IntegerField(default=0,verbose_name='Цена')

    def __str__(self):
        return (str(self.name_kart)+'--'+str(self.price_kart)+'руб')


class Samsung(models.Model):

    name_kart = models.CharField(max_length=50, default='', verbose_name='Наименование')

    price_kart = models.IntegerField(default=0,verbose_name='Цена')

    def __str__(self):
        return (str(self.name_kart)+'--'+str(self.price_kart)+'руб')
