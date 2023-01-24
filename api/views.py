from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer, CompEmpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    
    #/company/{company id}/employee
    
    @action(detail=True, methods=['get'])
    def employee(self,request, pk=None):
        comp=Company.objects.get(pk=pk)
        emp = Employee.objects.filter(c_id_id=comp)
        emp_Serializer = EmployeeSerializer(emp, many=True, context={'request':request})
        return Response(emp_Serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class CompanyGeneric(viewsets.generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    def get(self, request):
        result_list = self.serializer_class(self.get_queryset(), many=True)
        return Response(result_list.data)


class CompanyEmployeeGeneric(viewsets.generics.GenericAPIView):
    queryset = Company.objects.all()
    # serializer_class = CompEmpSerializer
    def get(self, request,pk):
        result_list = self.get_queryset().filter(company_id=pk).first()
        if not result_list:
            return Response({'message':'Not Found'}, status=400)
        serializer = CompEmpSerializer(result_list)
        return Response(serializer.data)
