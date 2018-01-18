# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0015_auto_20180117_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='scholar',
        ),
        migrations.AddField(
            model_name='collection',
            name='scholar',
            field=models.ManyToManyField(to='scholar.Scholar'),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Female'), (0, 'Male')], null=True),
        ),
    ]