# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-16 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='g3wcachinglayer',
            name='tilestache_layer_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]