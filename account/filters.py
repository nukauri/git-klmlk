import django_filters
from django import forms

from .models import Account,PayType,DocumentType,Project,Supplier,Banka
from area.models import Area


INPUT_CLASSES = 'w-full px-1 rounded-l border bg-gray-200'
PRICE_CLASSES = 'w-16 px-1 mt-4 rounded-l border bg-gray-200'
DATE_CLASSES = 'w-20 px-1 mt-4 rounded-l border bg-gray-200'

class AccountFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        label='Açıklama',
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': INPUT_CLASSES})
        )
    documentDate = django_filters.DateFromToRangeFilter(
        label='Tarih',
        widget=django_filters.widgets.RangeWidget(
            attrs={'class': DATE_CLASSES,'type': 'date'}
            ))
    price = django_filters.RangeFilter(
        label='Tutar',
        widget=django_filters.widgets.RangeWidget(
            attrs={'class': PRICE_CLASSES}
            ))
    payType = django_filters.ModelChoiceFilter(
        queryset=PayType.objects.all(),
        empty_label="Hepsi",
        label="Ödeme Tipi",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    documentType = django_filters.ModelChoiceFilter(
        queryset=DocumentType.objects.all(),
        empty_label="Hepsi",
        label="Doküman Tipi",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    area = django_filters.ModelChoiceFilter(
        queryset=Area.objects.all(),
        empty_label="Hepsi",
        label="Birim",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    banka = django_filters.ModelChoiceFilter(
        queryset=Banka.objects.all(),
        empty_label="Hepsi",
        label="Banka",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )

    supplier = django_filters.ModelChoiceFilter(
        queryset=Supplier.objects.all(),
        empty_label="Hepsi",
        label="Tedarikçi",
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
        )
    class Meta:
        model=Account
        fields=['documentDate','area','documentType','payType','banka','price','supplier','description']