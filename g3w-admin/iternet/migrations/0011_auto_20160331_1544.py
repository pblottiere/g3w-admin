# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import iternet.mixins.models


class Migration(migrations.Migration):

    dependencies = [
        ('iternet', '0010_civiciinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessiInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_acc', models.CharField(blank=True, max_length=15, null=True)),
                ('tip_opz', models.CharField(blank=True, choices=[('U', 'aggiornato'), ('I', 'nuovo inserimento'), ('D', 'cancellato')], max_length=1, null=True)),
            ],
            options={
                'db_table': 'accessi_info',
                'verbose_name': 'Accessi info',
                'verbose_name_plural': 'Accessi info',
            },
        ),
        migrations.CreateModel(
            name='LegCodClassifica',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_cod_classifica',
                'verbose_name': 'Legenda COD_CLASSIFICA tabella numero civico',
                'verbose_name_plural': 'Legenda COD_CLASSIFICA tabella numero civico',
            },
            bases=(iternet.mixins.models.LegIternetModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LegOneWay',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_one_way',
                'verbose_name': 'Legenda ONE_WAY tabella elemento stradale',
                'verbose_name_plural': 'Legenda ONE_WAY tabella elemento stradale',
            },
            bases=(iternet.mixins.models.LegIternetModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LegTipPav',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leg_tip_pav',
                'verbose_name': 'Legenda ONE_WAY tabella elemento stradale',
                'verbose_name_plural': 'Legenda ONE_WAY tabella elemento stradale',
            },
            bases=(iternet.mixins.models.LegIternetModelMixin, models.Model),
        ),
        migrations.RenameModel(
            old_name='LegDug',
            new_name='LegCodDug',
        ),
        migrations.AlterModelOptions(
            name='legcoddug',
            options={'verbose_name': 'Legenda COD_DUG tabella toponimo stradale', 'verbose_name_plural': 'Legenda DUG tabella toponimo stradale'},
        ),
        migrations.RenameField(
            model_name='archiinfo',
            old_name='cod_ele_new',
            new_name='cod_ele',
        ),
        migrations.RenameField(
            model_name='toponimostradale',
            old_name='dug',
            new_name='cod_dug',
        ),
        migrations.RemoveField(
            model_name='archiinfo',
            name='cod_ele_old',
        ),
        migrations.RemoveField(
            model_name='toponimostradale',
            name='cod_top2',
        ),
        migrations.RemoveField(
            model_name='toponimostradale',
            name='den_senza',
        ),
        migrations.AlterField(
            model_name='archiinfo',
            name='tip_opz',
            field=models.CharField(blank=True, choices=[('U', 'aggiornato'), ('I', 'nuovo inserimento'), ('D', 'cancellato')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='civiciinfo',
            name='tip_opz',
            field=models.CharField(blank=True, choices=[('U', 'aggiornato'), ('I', 'nuovo inserimento'), ('D', 'cancellato')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='toponimiinfo',
            name='tip_opz',
            field=models.CharField(blank=True, choices=[('U', 'aggiornato'), ('I', 'nuovo inserimento'), ('D', 'cancellato')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='elementostradale',
            name='one_way',
            field=models.ForeignKey(blank=True, db_column='one_way', null=True, on_delete=django.db.models.deletion.CASCADE, to='iternet.LegOneWay'),
        ),
        migrations.AddField(
            model_name='elementostradale',
            name='tip_pav',
            field=models.ForeignKey(blank=True, db_column='tip_pav', null=True, on_delete=django.db.models.deletion.CASCADE, to='iternet.LegTipPav'),
        ),
        migrations.AddField(
            model_name='numerocivico',
            name='cod_classifica',
            field=models.ForeignKey(blank=True, db_column='cod_classifica', null=True, on_delete=django.db.models.deletion.CASCADE, to='iternet.LegCodClassifica'),
        ),
    ]
