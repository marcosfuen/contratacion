# Generated by Django 2.2.5 on 2019-09-24 02:23

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractNumber', models.CharField(max_length=250, verbose_name='Número de contrato')),
                ('supplement', models.CharField(choices=[('S-1', 'S-1'), ('S-2', 'S-2'), ('S-3', 'S-3'), ('S-4', 'S-4'), ('S-5', 'S-5'), ('S-6', 'S-6'), ('S-7', 'S-7'), ('S-8', 'S-8'), ('S-9', 'S-9'), ('S-10', 'S-10')], max_length=250, verbose_name='Suplemento')),
                ('startDate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inicio')),
                ('endDate', models.DateTimeField(verbose_name='Vence')),
                ('headline', models.CharField(max_length=250, verbose_name='Titular')),
                ('contractType', models.CharField(max_length=250, verbose_name='Tipo de Contrato')),
                ('address', models.TextField(max_length=100, null=True, verbose_name='Dirección')),
                ('paymentType', models.CharField(choices=[('Factura', 'Factura'), ('Transferencia Bancaria', 'Transferencia Bancaria'), ('Factura o Conduce', 'Factura o Conduce'), ('Oferta', 'Oferta'), ('Pre-Factura', 'Pre-Factura')], max_length=100, verbose_name='Forma de pago')),
            ],
            options={
                'verbose_name': 'Contrato Vigente',
                'verbose_name_plural': 'Contratos Vigentes',
            },
        ),
        migrations.CreateModel(
            name='PrivateContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractNumber', models.CharField(max_length=250, verbose_name='Número de contrato')),
                ('supplement', models.CharField(choices=[('S-1', 'S-1'), ('S-2', 'S-2'), ('S-3', 'S-3'), ('S-4', 'S-4'), ('S-5', 'S-5'), ('S-6', 'S-6'), ('S-7', 'S-7'), ('S-8', 'S-8'), ('S-9', 'S-9'), ('S-10', 'S-10')], max_length=250, verbose_name='Suplemento')),
                ('startDate', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Inicio')),
                ('endDate', models.DateTimeField(verbose_name='Vence')),
                ('patentNumber', models.CharField(max_length=250, verbose_name='Número de patente')),
                ('headline', models.CharField(max_length=250, verbose_name='Titular')),
                ('ciNumber', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+\\Z'), " Oops, Introdusca un 'NÚMERO DE CARNET IDENTIDAD' válido, solo consiste en números y de longitud 11 carácteres.", 'error')], verbose_name='Carnet Identidad')),
                ('address', models.TextField(max_length=100, null=True, verbose_name='Dirección')),
                ('patentConcept', models.CharField(choices=[('Compraventa', 'Compraventa'), ('Reparacion y Mantenimiento de inmuebles', 'Reparacion y Mantenimiento de inmuebles'), ('Prestacion de Servicio de alli estan los siguientes servicio', 'Prestacion de Servicio de alli estan los siguientes servicio'), ('Servicos de Arrendamiento de habitaciones', 'Servicos de Arrendamiento de habitaciones'), ('Servcio de Alojamiento Habitaciones', 'Servcio de Alojamiento Habitaciones'), ('Servicio de Mecanografia', 'Servicio de Mecanografia'), ('Alquiler de Salones', 'Alquiler de Salones'), ('Rotulista Grabador', 'Rotulista Grabador'), ('Servcio de Alimentacion', 'Servcio de Alimentacion'), ('Servicio de transportacion', 'Servicio de transportacion'), ('Impresion', 'Impresion'), ('Servicios Artisticos', 'Servicios Artisticos'), ('Servicio de Arreglos florales', 'Servicio de Arreglos florales'), ('Servico de Reparacion y Mantenimiento', 'Servico de Reparacion y Mantenimiento'), ('Oprador de Audio', 'Oprador de Audio'), ('Servicio de cooperacion', 'Servicio de cooperacion'), ('Decoradores', 'Decoradores'), ('Servicio decomiso', 'Servicio decomiso'), ('Servicios de traduccion', 'Servicios de traduccion'), ('Servicio de Eventos', 'Servicio de Eventos'), ('Servicio de Plomerias', 'Servicio de Plomerias'), ('Servicios gastronomicos', 'Servicios gastronomicos'), ('Albañil', 'Albañil'), ('Servicio de uso de aguas', 'Servicio de uso de aguas'), ('Cerrajero', 'Cerrajero'), ('Servicio de alcantarrillado', 'Servicio de alcantarrillado'), ('productor y vendedor de articulos varios', 'productor y vendedor de articulos varios'), ('Servicio de pago de consumo electrico', 'Servicio de pago de consumo electrico'), ('Servicio de chapisteria', 'Servicio de chapisteria'), ('Servicio de Tapiceria', 'Servicio de Tapiceria'), ('Servico de Electricidad', 'Servico de Electricidad')], max_length=250, verbose_name='Concepto de la patente')),
                ('value', models.FloatField(default=0, verbose_name='Monto de pago')),
                ('paymentType', models.CharField(choices=[('cup', 'CUP'), ('cuc', 'CUC')], max_length=100, verbose_name='Tipo de pago')),
            ],
            options={
                'verbose_name': 'Contrato de cuenta propia',
                'verbose_name_plural': 'Contratos de cuenta propia',
            },
        ),
    ]
