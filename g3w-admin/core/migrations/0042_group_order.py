# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20170919_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]