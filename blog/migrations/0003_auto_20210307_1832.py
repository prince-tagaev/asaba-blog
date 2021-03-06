# Generated by Django 3.1.3 on 2021-03-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210307_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shop_sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=2),
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название статьи'),
        ),
    ]
