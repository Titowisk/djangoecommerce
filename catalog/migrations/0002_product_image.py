# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-08 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagem'),
        ),
    ]
