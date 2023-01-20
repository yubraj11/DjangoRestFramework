from django.shortcuts import render
from rest_framework import viewsets
from api.models import company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer

    
    #/company/{company id}/employee
    
    @action(detail=True, methods=['get'])
    def employee(self,request, pk=None):
        comp=company.objects.get(pk=pk)
        emp = Employee.objects.filter(c_id_id=comp)
        emp_Serializer = EmployeeSerializer(emp, many=True, context={'request':request})
        return Response(emp_Serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer