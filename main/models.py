from django.db import models

# case 
# cpu
# mainboard
# video card
# ram
# ssd
# cooler
# power supply unit


class Case(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class CPU(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class Mainboard(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class VideoCard(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class RAM(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class SSD(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class HDD(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class Cooler(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class PowerSupplyUnit(models.Model):

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.name


class Complete_PC(models.Model):
    
    cpu = models.CharField(max_length=255, verbose_name='Процеоср')
    videoCard = models.CharField(max_length=255, verbose_name='Відео карта')
    ram = models.CharField(max_length=255, verbose_name='Оперативна пам"ять')
    memory = models.CharField(max_length=255, verbose_name='Внутрішній накопичувач')
    mainBoard = models.CharField(max_length=255, verbose_name='Материнська плата')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    img = models.ImageField(verbose_name='Зображення')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')

    def __str__(self):
        return self.cpu
