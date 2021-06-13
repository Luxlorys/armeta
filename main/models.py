from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    class Meta:
        abstract=True

    name = models.CharField(max_length=255, verbose_name='Назва товару')
    description = models.TextField(null=False, verbose_name='Опис товару', default='')
    img = models.ImageField(verbose_name='Зображення')
    price = models.IntegerField(null=False, verbose_name='Ціна')
    link = models.TextField(null=False, verbose_name='Посилання на товар', default='')    

class Case(Product):

    def __str__(self):
        return self.name

class CPU(Product):

    def __str__(self):
        return self.name

class Mainboard(Product):

    def __str__(self):
        return self.name

class VideoCard(Product):

    def __str__(self):
        return self.name

class RAM(Product):

    def __str__(self):
        return self.name

class SSD(Product):

    def __str__(self):
        return self.name

class HDD(Product):

    def __str__(self):
        return self.name

class Cooler(Product):

    def __str__(self):
        return self.name

class PowerSupplyUnit(Product):

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


class add_to_cart(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)