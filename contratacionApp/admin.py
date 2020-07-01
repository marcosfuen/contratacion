from django.contrib import admin
from .models import PrivateContract, CurrentContract, AuditCurrentContract, AuditPrivateContract
from contratacionApp.models import PatentConcept, Supplement
from ipware import get_client_ip
from django.core.exceptions import ValidationError

# Register your models here.
class PrivateContractAdmin(admin.ModelAdmin):
    list_display = ('numberRegistration', 'expired', 'contractNumber', 'Suplemento', 'startDate', 'endDate', 'patentNumber', 'headline', 'ciNumber', 'address', 'patentConcept', 'value', 'paymentType', 'upLoadFile')
    list_display_links = ('numberRegistration', 'contractNumber', 'expired')
    filter_horizontal = ('supplement', )
    search_fields = ['numberRegistration', 'headline', 'contractNumber', 'patentNumber', 'supplement__name', 'patentConcept__name', 'ciNumber', 'startDate', 'endDate']
    fieldsets = [
        ('Datos Generales',  {'fields': ['numberRegistration', 'contractNumber', 'supplement', 'startDate', 'endDate']}),
        ('Empresa o Persona',{'fields': ['patentNumber', 'headline', 'ciNumber', 'address', 'patentConcept', 'value', 'paymentType','upLoadFile', 'expired']}),
    ]
    def Suplemento(self, obj):
        return ", ".join([str(supplement.name) for supplement in obj.supplement.all()])

    def save_model(self, request, obj, form, change):
        auditPrivateContract = None
        if obj.id:
            objUser = request.user
            client_ip, is_routable = get_client_ip(request)
            auditPrivateContract = AuditPrivateContract(ip=client_ip, userName=objUser, numberRegistration=obj.numberRegistration, contractNumber=obj.contractNumber, newStartDate=obj.startDate, newEndDate=obj.endDate, action='Se modificó el contrato con estos datos', patentNumber=obj.patentNumber, headline=obj.headline, ciNumber=obj.ciNumber, address=obj.address, patentConcept=obj.patentConcept, value=obj.value, paymentType=obj.paymentType, expired=obj.expired)
            # auditCurrentContract = AuditCurrentContract(ip=client_ip, userName=objUser, contractNumber='contractNumber', newStartDate='startDate', newEndDate='endDate', action='Actualizo el contrato con estos datos', headline='headline', address='address',  paymentType='paymentType', expired='expired')
            try:
                auditPrivateContract.save()
            except ValidationError:
                return
            auditPrivateContract.supplement.set(form.cleaned_data['supplement'])
            super().save_model(request, obj, form, change)
        elif not obj.id or obj.id is None:
            objUser = request.user
            client_ip, is_routable = get_client_ip(request)
            auditPrivateContract = AuditPrivateContract(ip=client_ip, userName=objUser.username, numberRegistration=obj.numberRegistration, contractNumber=obj.contractNumber, newStartDate=obj.startDate, newEndDate=obj.endDate, action='Se adiciona un contrato nuevo con estos datos', patentNumber=obj.patentNumber, headline=obj.headline, ciNumber=obj.ciNumber, address=obj.address, patentConcept=obj.patentConcept, value=obj.value, paymentType=obj.paymentType, expired=obj.expired)
            try:
                auditPrivateContract.save()
            except ValidationError:
                return
            auditPrivateContract.supplement.set(form.cleaned_data['supplement'])
            super().save_model(request, obj, form, change)

class CurrentContractAdmin(admin.ModelAdmin):
    list_display = ('numberRegistration', 'expired', 'contractNumber', 'Suplemento', 'startDate', 'endDate', 'headline', 'address', 'contractType', 'paymentType', 'upLoadFile')
    filter_horizontal = ('supplement', )
    list_display_links = ('numberRegistration', 'contractNumber', 'expired')
    search_fields = ['numberRegistration', 'headline', 'supplement__name', 'contractNumber', 'contractType__name', 'startDate', 'endDate']
    fieldsets = [
        ('Datos Generales',  {'fields': ['numberRegistration', 'contractNumber', 'supplement', 'startDate', 'endDate']}),
        ('Empresa o Persona',{'fields': ['headline', 'address', 'contractType', 'paymentType', 'upLoadFile', 'expired']}),
    ]
    def Suplemento(self, obj):
        return ", ".join([str(supplement.name) for supplement in obj.supplement.all()])
        
    def save_model(self, request, obj, form, change):
        if obj.id:
            objUser = request.user
            client_ip, is_routable = get_client_ip(request)
            auditCurrentContract = AuditCurrentContract(ip=client_ip, userName=objUser, numberRegistration=obj.numberRegistration, contractNumber=obj.contractNumber, newStartDate=obj.startDate, newEndDate=obj.endDate, action='Se Modificó el contrato con estos datos', headline=obj.headline, address=obj.address, contractType=obj.contractType, paymentType=obj.paymentType, expired=obj.expired)
            try:
                auditCurrentContract.save()
            except ValidationError:
                return
            auditCurrentContract.supplement.set(form.cleaned_data['supplement'])
            super().save_model(request, obj, form, change)            
        elif not obj.id:
            objUser = request.user
            client_ip, is_routable = get_client_ip(request)
            auditCurrentContract = AuditCurrentContract(ip=client_ip, userName=objUser, numberRegistration=obj.numberRegistration, contractNumber=obj.contractNumber, newStartDate=obj.startDate, newEndDate=obj.endDate, action='Se adiciona un contrato nuevo con estos datos', headline=obj.headline, address=obj.address, contractType=obj.contractType, paymentType=obj.paymentType, expired=obj.expired)
            try:
                auditCurrentContract.save()
            except ValidationError:
                return
            auditCurrentContract.supplement.set(form.cleaned_data['supplement'])
            super().save_model(request, obj, form, change)
            
class PatentConceptAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuditCurrentContractAdmin(admin.ModelAdmin):
    list_display = ('action', 'ip', 'userName', 'numberRegistration', 'contractNumber', 'Suplemento', 'newStartDate', 'newEndDate', 'headline', 'address', 'contractType', 'paymentType', 'expired')
    search_fields = ['numberRegistration', 'headline', 'ip', 'userName', 'contractNumber',]

    def Suplemento(self, obj):
        return ", ".join([str(supplement.name) for supplement in obj.supplement.all()])

class AuditPrivateContractAdmin(admin.ModelAdmin):
    list_display = ('action', 'ip', 'userName', 'numberRegistration', 'contractNumber', 'Suplemento', 'newStartDate', 'newEndDate', 'patentNumber', 'headline', 'ciNumber', 'address', 'patentConcept', 'value', 'paymentType', 'expired')
    search_fields = ['numberRegistration', 'headline', 'ip', 'userName', 'contractNumber', 'patentNumber']

    def Suplemento(self, obj):
        return ", ".join([str(supplement.name) for supplement in obj.supplement.all()])




admin.site.register(PatentConcept, PatentConceptAdmin)
admin.site.register(PrivateContract, PrivateContractAdmin)
admin.site.register(CurrentContract, CurrentContractAdmin)
admin.site.register(AuditCurrentContract, AuditCurrentContractAdmin)
admin.site.register(AuditPrivateContract, AuditPrivateContractAdmin)
admin.site.register(Supplement)




admin.site.site_header = 'Contratación - Administración'
admin.site.site_title = 'Sistema de Contratación - Administración'