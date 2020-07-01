from rest_framework import viewsets, filters
from .serializers import CurrentContractSerializer, PrivateContractSerializer
from contratacionApp.models import PrivateContract, CurrentContract
from rest_framework.decorators import action
from datetime import datetime
from django.db.models import Q
from rest_framework.response import Response



class CurrentContractViewSet(viewsets.ModelViewSet):
    queryset = CurrentContract.objects.all()
    serializer_class = CurrentContractSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('numberRegistration', 'contractNumber', 'supplement__name', 'startDate', 'endDate', 'headline', 'address', 'paymentType', 'contractType__name')
    ordering_fields = ('id',)
    http_method_names = ['get', 'head']

    @action(detail=False, methods=['get'])
    def currentMonth(self, request):
        """
        Mostrar contratos por empresa del mes actual. 
        """
        # Filtrar actividades por fecha y dejar sólo las del mes actual
        today = datetime.today()
        self.queryset = self.get_queryset().filter(Q(startDate__year=today.year, startDate__month=today.month))

        # Aplicar otros filtros del viewset
        queryset = self.filter_queryset(self.queryset)

        # # Paginar resultados
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # Serializar resultados
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PrivateContractViewSet(viewsets.ModelViewSet):
    queryset = PrivateContract.objects.all()
    serializer_class = PrivateContractSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('numberRegistration', 'contractNumber', 'supplement__name', 'startDate', 'endDate', 'patentNumber', 'headline', 'ciNumber', 'address', 'value', 'paymentType', 'patentConcept__name')
    ordering_fields = ('id',)
    http_method_names = ['get', 'head']
    
    @action(detail=False, methods=['get'])
    def currentMonth(self, request):
        """
        Mostrar contratos por cuenta propia del mes actual.
        """
        # Filtrar actividades por fecha y dejar sólo las del mes actual
        today = datetime.today()
        self.queryset = self.get_queryset().filter(Q(startDate__year=today.year, startDate__month=today.month))

        # Aplicar otros filtros del viewset
        queryset = self.filter_queryset(self.queryset)

        # # Paginar resultados
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # Serializar resultados
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
