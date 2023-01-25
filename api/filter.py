from django_filters import rest_framework as filters 
from .models import Company
from django_filters.fields import MultipleChoiceField, CSVWidget


class MultipleField(MultipleChoiceField):
    def valid_value(self, value):
        True
    
class MultipleFilter(filters.MultipleChoiceFilter):
    field_class = MultipleField


class CompanyFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    # location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    
    class Meta:
        model = Company
        fields = {
            'name': ['contains'],
            'location':['contains']
        }

