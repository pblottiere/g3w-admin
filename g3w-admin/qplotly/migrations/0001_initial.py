# Generated by Django 2.2.13 on 2020-09-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qdjango', '0052_layer_download_csv'),
    ]

    operations = [
        migrations.CreateModel(
            name='QplotlyWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml', models.TextField(verbose_name='XML original settings')),
                ('datasource', models.TextField(verbose_name='Layer datasource')),
                ('selected_features_only', models.BooleanField(default=False, verbose_name='Use selected features only')),
                ('visible_features_only', models.BooleanField(default=False, verbose_name='Use visible features only')),
                ('layers', models.ManyToManyField(to='qdjango.Layer')),
            ],
        ),
    ]