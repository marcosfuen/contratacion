from rest_framework import serializers
from .models import PrivateContract, CurrentContract, PatentConcept, Supplement

class PatentConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatentConcept
        fields = ['name']

class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = ['id', 'name']

class CurrentContractSerializer(serializers.ModelSerializer):
    contractType = PatentConceptSerializer()
    supplement = SupplementSerializer(many=True)
    class Meta:
        model = CurrentContract
        fields = ['numberRegistration', 'expired', 'contractNumber', 'supplement', 'startDate', 'endDate', 'headline', 'address', 'contractType', 'paymentType', 'upLoadFile']

class PrivateContractSerializer(serializers.ModelSerializer):
    patentConcept = PatentConceptSerializer()
    supplement = SupplementSerializer(many=True)
    class Meta:
        model = PrivateContract
        fields = ['numberRegistration', 'expired', 'contractNumber', 'supplement', 'startDate', 'endDate', 'patentNumber', 'headline', 'ciNumber', 'address', 'patentConcept', 'value', 'paymentType', 'upLoadFile']