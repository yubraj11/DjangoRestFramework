from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet, CompanyGeneric, CompanyEmployeeGeneric
router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)
# router.register(r'compGen/', CompanyGeneric, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    path("compgen/", CompanyGeneric.as_view()),
    path("compgen/<int:pk>/", CompanyEmployeeGeneric.as_view()),

]
