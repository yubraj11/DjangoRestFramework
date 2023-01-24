from rest_framework import serializers
from api.models import Company, Employee

#create serializers here
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
    


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=["emp_id","name", "address", "email", "phone"]


class CompEmpSerializer(serializers.ModelSerializer):
    Employee_in_company = EmployeeSerializer(many=True, source="employee_set")
    class Meta:
        model = Company
        fields = ['company_id', 'name','location','about', 'type','added_date', 'active','Employee_in_company']
        