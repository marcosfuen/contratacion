from django.db import models
from django.core.validators import RegexValidator
import re
import datetime

# Create your models here.
class PatentConcept(models.Model):
    name = models.CharField('Nombre', max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return
    class Meta:
        verbose_name = 'Concepto de la patente'
        verbose_name_plural = 'Conceptos de las patentes o tipos' 

class Supplement(models.Model):
    name = models.CharField('Nombre Suplemento', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Suplemento'
        verbose_name_plural = 'Suplementos' 


class AuditCurrentContract(models.Model):
    ip = models.GenericIPAddressField()
    userName = models.CharField('Nombre', max_length=250, blank=True, null=True)
    numberRegistration = models.CharField('Número de Registro', max_length=250, blank=False, null=False, default=0)
    contractNumber = models.CharField('Número de contrato', max_length=250, blank=True, null=True)
    supplement = models.ManyToManyField(Supplement, max_length=250, verbose_name='Suplemento')
    newStartDate = models.DateTimeField('Fecha Inicio', default=datetime.datetime.now())
    newEndDate = models.DateTimeField('Fecha Vence', default=datetime.datetime.now())
    action = models.CharField('accion que realizo', max_length=250, blank=True, null=True)
    headline = models.CharField('Titular', max_length=250, default='')
    address = models.TextField('Dirección', max_length=100, null=True, blank=True,)
    contractType = models.ForeignKey(PatentConcept, verbose_name='Tipo de Contrato', on_delete=models.SET_NULL, blank=True, null=True)
    paymentType = models.CharField('Forma de pago', max_length = 100, default='')
    expired = models.BooleanField('Vencido', null=True, blank=True)

    class Meta:
        verbose_name = 'Auditoria Contrato Empresa'
        verbose_name_plural = 'Auditoria de Contratos Empresas'

class AuditPrivateContract(models.Model):
    ip = models.GenericIPAddressField()
    userName = models.CharField('Nombre', max_length=250, blank=True, null=True)
    numberRegistration = models.CharField('Número de Registro', max_length=250, blank=False, null=False, default=0)
    contractNumber = models.CharField('Número de contrato', max_length=250, blank=True, null=True)
    supplement = models.ManyToManyField(Supplement, max_length=250, verbose_name='Suplemento')
    newStartDate = models.DateTimeField('Fecha Inicio', default=datetime.datetime.now())
    newEndDate = models.DateTimeField('Fecha Vence', default=datetime.datetime.now())
    action = models.CharField('accion que realizo', max_length=250, blank=True, null=True)
    patentNumber = models.CharField('Número de patente', max_length=250)
    headline = models.CharField('Titular', max_length=250, default='')
    ciNumber = models.CharField('Carnet Identidad', max_length=11, blank=True)
    address = models.TextField('Dirección', max_length=100, null=True, blank=True,)
    patentConcept = models.ForeignKey(PatentConcept, verbose_name='Concepto de la patente', on_delete=models.SET_NULL, blank=True, null=True)
    value = models.FloatField('Monto de pago' ,default=0)
    paymentType = models.CharField('Forma de pago', max_length = 100, default='')
    expired = models.BooleanField('Vencido', null=True, blank=True)

    class Meta:
        verbose_name = 'Auditoria Contrato de cuenta propia'
        verbose_name_plural = 'Auditoria de Contratos de cuenta propia' 

class CurrentContract(models.Model):

    paymentTypeChoise = (
        ('Factura', 'Factura'),
        ('Transferencia Bancaria', 'Transferencia Bancaria'),
        ('Factura o Conduce', 'Factura o Conduce'),
        ('Oferta', 'Oferta'),
        ('Pre-Factura', 'Pre-Factura')        
    )
    numberRegistration = models.CharField('Número de Registro', max_length=250, blank=False, null=False, default=0)
    contractNumber = models.CharField('Número de contrato', max_length=250, blank=False, null=False)
    supplement = models.ManyToManyField(Supplement, max_length=250, verbose_name='Suplemento', blank=True)
    startDate = models.DateTimeField('Fecha Inicio', default=datetime.datetime.now())
    endDate = models.DateTimeField('Fecha Vence', default=datetime.datetime.now())
    headline = models.CharField('Titular', max_length=250)
    address = models.TextField('Dirección', max_length=100, null=True, blank=False,)
    contractType = models.ForeignKey(PatentConcept, verbose_name='Tipo de Contrato', on_delete=models.SET_NULL, blank=True, null=True)
    paymentType = models.CharField('Forma de pago', max_length = 100, choices = paymentTypeChoise,)
    upLoadFile = models.FileField('Ficheros del contrato',null=True, blank=True)
    expired = models.BooleanField('Vencido', null=True, blank=True)

    def __str__(self):
        return self.contractNumber 

    def __unicode__(self):
        return


    class Meta:
        verbose_name = 'Contrato Empresa'
        verbose_name_plural = 'Contratos Empresas' 
        ordering = ['id'] 

class PrivateContract(models.Model):
    expreRegular = re.compile(r'^[0-9]+\Z')
    validateCampoCI = RegexValidator(
        expreRegular,
        " Oops, Introdusca un 'NÚMERO DE CARNET IDENTIDAD' válido, solo consiste en números y de longitud 11 carácteres.",
        'error'
    )
    paymentTypeChoise = (
        ('cup', 'CUP'),
        ('cuc', 'CUC'),        
    )
    numberRegistration = models.CharField('Número de Registro', max_length=250, blank=False, null=False, default=0)
    contractNumber = models.CharField('Número de contrato', max_length=250, blank=False, null=False)
    supplement = models.ManyToManyField(Supplement, max_length=250, verbose_name='Suplemento', blank=True)
    startDate = models.DateTimeField('Fecha Inicio', default=datetime.datetime.now())
    endDate = models.DateTimeField('Fecha Vence', default=datetime.datetime.now())
    patentNumber = models.CharField('Número de patente', max_length=250)
    headline = models.CharField('Titular', max_length=250)
    ciNumber = models.CharField('Carnet Identidad', max_length=11, unique=True, blank=False, validators=[validateCampoCI])
    address = models.TextField('Dirección', max_length=100, null=True, blank=False,)
    patentConcept = models.ForeignKey(PatentConcept, verbose_name='Concepto de patente', on_delete=models.SET_NULL, blank=True, null=True)
    value = models.FloatField('Monto de pago' ,default=0)
    paymentType = models.CharField('Tipo de pago', max_length = 100, choices = paymentTypeChoise,)
    upLoadFile = models.FileField('Ficheros del contrato',null=True, blank=True)
    expired = models.BooleanField('Vencido', null=True, blank=True)

    def __str__(self):
        return self.contractNumber

    def __unicode__(self):
        return
    
    class Meta:
        verbose_name = 'Contrato de cuenta propia'
        verbose_name_plural = 'Contratos de cuenta propia' 
        ordering = ['id']
