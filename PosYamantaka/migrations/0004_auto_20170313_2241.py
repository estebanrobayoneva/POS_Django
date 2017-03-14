# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PosYamantaka', '0003_auto_20170313_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='porcentaje_descuento',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='categorias',
            field=models.ManyToManyField(blank=True, null=True, through='PosYamantaka.Discount', to='PosYamantaka.Category'),
        ),
        migrations.AlterField(
            model_name='society',
            name='valor_anual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='valor_mensual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='valor_semestral',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
