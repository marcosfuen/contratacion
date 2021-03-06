# Generated by Django 2.2.5 on 2020-02-12 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0028_auto_20200211_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditcurrentcontract',
            options={'verbose_name': 'Auditoria Contrato Empresa', 'verbose_name_plural': 'Auditoria de Contratos Empresas'},
        ),
        migrations.AlterModelOptions(
            name='auditprivatecontract',
            options={'verbose_name': 'Auditoria Contrato de cuenta propia', 'verbose_name_plural': 'Auditoria de Contratos de cuenta propia'},
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 435602), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 435602), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 437600), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 437600), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 439598), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 439598), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 442596), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 13, 25, 442596), verbose_name='Fecha Inicio'),
        ),
    ]
