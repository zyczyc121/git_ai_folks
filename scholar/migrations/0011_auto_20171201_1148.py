# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0010_auto_20171130_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
