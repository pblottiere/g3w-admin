# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iternet', '0023_auto_20160415_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_catastale', models.CharField(max_length=6, null=True)),
                ('denominazione', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
