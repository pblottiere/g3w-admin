# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160229_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProjectPanoramic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(max_length=255, verbose_name='Project type')),
                ('project_id', models.IntegerField(verbose_name='Project type id')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_panoramic', to='core.Group', verbose_name='Group')),
            ],
        ),
    ]
