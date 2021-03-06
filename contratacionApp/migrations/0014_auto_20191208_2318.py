# Generated by Django 2.2.5 on 2019-12-09 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0013_auto_20191208_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditcurrentcontract',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='auditcurrentcontract',
            name='startDate',
        ),
        migrations.AddField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 802034), verbose_name='Fecha Vence'),
        ),
        migrations.AddField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 801981), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 802951), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 802912), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 804672), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 18, 44, 804632), verbose_name='Fecha Inicio'),
        ),
    ]
