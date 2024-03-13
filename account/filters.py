import django_filters
from django import forms

from .models import Account,DocumentGroup,DocumentType,Project,Supplier
from area.models import Area
from accomodation.models import Accomodation

INPUT_CLASSES = 'w-full px-1 rounded-l border bg-gray-200'
PRICE_CLASSES = 'w-16 px-1 mt-4 rounded-l border bg-gray-200'

class AccountFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        label='Açıklama',
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES})
        )
    price = django_filters.RangeFilter(
        label='Price range',
        widget=django_filters.widgets.RangeWidget(
            attrs={'class': PRICE_CLASSES}
            ))
    documentGroup = django_filters.ModelChoiceFilter(
        queryset=DocumentGroup.objects.all(),
        empty_label="All Groups",
        label="DocumentGroups",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    documentType = django_filters.ModelChoiceFilter(
        queryset=DocumentType.objects.all(),
        empty_label="All TYpes",
        label="DocumentTypes",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    area = django_filters.ModelChoiceFilter(
        queryset=Area.objects.all(),
        empty_label="All TYpes",
        label="Areas",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    accomodation = django_filters.ModelChoiceFilter(
        queryset=Accomodation.objects.all(),
        empty_label="All TYpes",
        label="Konaklama",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    project = django_filters.ModelChoiceFilter(
        queryset=Project.objects.all(),
        empty_label="All TYpes",
        label="Projeler",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    supplier = django_filters.ModelChoiceFilter(
        queryset=Supplier.objects.all(),
        empty_label="All TYpes",
        label="Tedarikçi",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    class Meta:
        model=Account
        fields=['documentGroup','documentType','description','price','area','accomodation','project','supplier']