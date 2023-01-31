from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer, CompEmpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .pagination import DynamicPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import CompanyFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    pagination_class = DynamicPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_class = CompanyFilter
    search_fields = ['name', 'location']  
    filterset_fields = ['name', 'location']

    
    #/company/{company id}/employee
    
    @action(detail=True, methods=['get'])
    def employee(self,request, pk=None):
        comp=Company.objects.get(pk=pk)
        emp = Employee.objects.filter(c_id_id=comp)
        emp_Serializer = EmployeeSerializer(emp, many=True, context={'request':request})
        return Response(emp_Serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class = DynamicPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['emp_id','name', 'address']

class CompanyGeneric(viewsets.generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    queryset = Company.objects.all()
    # pagination_class = DynamicPagination
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_class = CompanyFilter
    search_fields = ['name', 'location','about']  
    filterset_fields = ['name', 'location']
    def get(self, request):
        filter_list = self.filter_queryset(self.get_queryset())

#core coding for filterset to filter data with lowercase as well as uppercase 
        
        if request.GET.get('name'):
            if not filter_list:
                filter_list = self.get_queryset().filter(name__icontains=request.GET.get('name')) 

        result_list = self.paginate_queryset(filter_list)
        serializer = self.serializer_class(result_list, many=True)
        return self.get_paginated_response(serializer.data)

class CompanyEmployeeGeneric(viewsets.generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Company.objects.all()
    pagination_class = PageNumberPagination 
    # serializer_class = CompEmpSerializer
    def get(self, request,pk):
        result_list = self.get_queryset().filter(company_id=pk).first()
        if not result_list:
            return Response({'message':'Not Found'}, status=400)
        serializer = CompEmpSerializer(result_list)
        return Response(serializer.data)
