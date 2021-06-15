from django.db import models
from django.contrib.auth.models import User

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

class product_category(models.Model):

    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class add_to_cart(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Замовлення № {self.id}'

class Product_details(models.Model):

    product_name = models.CharField(max_length=60)
    category_name = models.ForeignKey(product_category, on_delete = models.CASCADE, null=True)
    product_img1 = models.ImageField()
    product_description = models.TextField(max_length=5000,null=True)
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_name