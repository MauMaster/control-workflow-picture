
import django_filters
from django import forms
from bootstrap_datepicker_plus import  DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from .models import (
    Images,
    Photographers,
    Payment
)



class ImagesFilter(django_filters.FilterSet):
    checkin = django_filters.NumberFilter(widget=DatePickerInput(format='%d'),field_name='checkin', lookup_expr='day'  )
    checkin1 = django_filters.NumberFilter(widget=DatePickerInput(format='%m'),field_name='checkin', lookup_expr='month'  )
    checkin2 = django_filters.NumberFilter(widget=DatePickerInput(format='%Y'),field_name='checkin', lookup_expr='year'  )
    # usando o name__photographers eu estou dizendo que quero busca o name da tabela photographes, desse modo terei um boxlistt em meu template
    name__photographers =  django_filters.CharFilter(lookup_expr='icontains', field_name='name')
     
    class Meta:
        model = Images
        fields = ['name', 'checkin']

class PaymentFilter(django_filters.FilterSet):
    checkin1 = django_filters.NumberFilter(widget=DatePickerInput(format='%m'),field_name='checkin', lookup_expr='month'  )
    checkin2 = django_filters.NumberFilter(widget=DatePickerInput(format='%Y'),field_name='checkin', lookup_expr='year'  )
        
    
    # usando o name__photographers eu estou dizendo que quero busca o name da tabela photographes, desse modo terei um boxlistt em meu template
    name__photographers =  django_filters.CharFilter(lookup_expr='icontains', field_name='name')
     
    class Meta:
        model = Payment
        fields = ['name', 'checkin']

