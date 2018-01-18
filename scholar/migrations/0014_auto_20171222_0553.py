# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-22 05:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0013_scholar_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_json', django.contrib.postgres.fields.jsonb.JSONField(default=None, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='scholar',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Female'), (0, 'Male')], null=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='scholar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scholar.Scholar'),
        ),
    ]