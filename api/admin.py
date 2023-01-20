from django.contrib import admin
from api.models import company, Employee
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','address','c_id')

admin.site.register(company, CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
