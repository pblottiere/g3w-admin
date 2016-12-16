# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-16 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20161115_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSuiteData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtitle')),
                ('home_description', models.TextField(blank=True, null=True, verbose_name='Home description')),
                ('about_description', models.TextField(blank=True, null=True, verbose_name='About description')),
                ('about_name', models.CharField(max_length=255, verbose_name='About name')),
                ('about_tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='About name')),
                ('about_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='About email')),
                ('about_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='About address')),
                ('groups_map_description', models.TextField(blank=True, null=True, verbose_name='Groups map description')),
                ('login_description', models.TextField(blank=True, null=True, verbose_name='Login description')),
                ('suite_logo', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Suite logo')),
            ],
        ),
    ]
