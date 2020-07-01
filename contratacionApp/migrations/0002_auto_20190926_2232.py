# Generated by Django 2.2.5 on 2019-09-27 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Número de contrato')),
            ],
            options={
                'verbose_name': 'Concepto de la patente',
                'verbose_name_plural': 'Conceptos de las patentes',
            },
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='patentConcept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contratacionApp.PatentConcept', verbose_name='Concepto de la patente'),
        ),
    ]