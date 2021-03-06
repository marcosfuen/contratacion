# Generated by Django 2.2.5 on 2020-02-17 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0030_auto_20200211_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currentcontract',
            options={'ordering': ['id'], 'verbose_name': 'Contrato Empresa', 'verbose_name_plural': 'Contratos Empresas'},
        ),
        migrations.AlterModelOptions(
            name='privatecontract',
            options={'ordering': ['id'], 'verbose_name': 'Contrato de cuenta propia', 'verbose_name_plural': 'Contratos de cuenta propia'},
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 950984), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 950984), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 952983), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 952983), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 955981), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 955981), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='supplement',
            field=models.ManyToManyField(blank=True, max_length=250, to='contratacionApp.Supplement', verbose_name='Suplemento'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 958978), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 14, 4, 32, 958978), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='supplement',
            field=models.ManyToManyField(blank=True, max_length=250, to='contratacionApp.Supplement', verbose_name='Suplemento'),
        ),
    ]
