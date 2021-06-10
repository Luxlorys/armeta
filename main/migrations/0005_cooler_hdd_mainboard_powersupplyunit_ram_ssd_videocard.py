# Generated by Django 3.1.6 on 2021-03-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210305_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='Mainboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='PowerSupplyUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('link', models.TextField(default='Some string', verbose_name='Ссылка на товар')),
            ],
        ),
    ]
