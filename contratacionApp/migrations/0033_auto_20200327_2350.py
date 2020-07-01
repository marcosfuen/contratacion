# Generated by Django 2.2.5 on 2020-03-28 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0032_auto_20200226_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 473467), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 473467), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 475465), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 475465), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 478463), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 478463), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 480461), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 23, 50, 26, 480461), verbose_name='Fecha Inicio'),
        ),
    ]
