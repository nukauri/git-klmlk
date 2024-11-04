from import_export import resources,fields
from .models import Account,DocumentType,PayType,Banka,Supplier,CurrencyUnit
from area.models import Area
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User

class AccountResource(resources.ModelResource):
    documentType =fields.Field(
        column_name='documentType',
        attribute='documentType',
        widget=ForeignKeyWidget(DocumentType,field='name')
    )
    payType =fields.Field(
        column_name='payType',
        attribute='payType',
        widget=ForeignKeyWidget(PayType,field='name')
    )
    banka =fields.Field(
        column_name='banka',
        attribute='banka',
        widget=ForeignKeyWidget(Banka,field='name')
    )
    currencyUnit =fields.Field(
        column_name='currencyUnit',
        attribute='currencyUnit',
        widget=ForeignKeyWidget(CurrencyUnit,field='name')
    )
    area =fields.Field(
        column_name='area',
        attribute='area',
        widget=ForeignKeyWidget(Area,field='name')
    )
    supplier =fields.Field(
        column_name='supplier',
        attribute='supplier',
        widget=ForeignKeyWidget(Supplier,field='name')
    )
    created_by =fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(User,field='name')
    )
    class Meta:
        model=Account
        fields = (
            'documentType',
            'payType',
            'banka',
            'documentDate',
            'description',
            'price',
            'currencyUnit',
            'area',
            'supplier',
            'created_by',
            'created_at',
        )