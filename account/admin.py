from django.contrib import admin

# Register your models here.

from .models import Supplier, DocumentType, Project, Account,PayType,Banka,Debit,CurrencyUnit

admin.site.register(Supplier)
admin.site.register(DocumentType)
admin.site.register(Project)
admin.site.register(Account)
admin.site.register(PayType)
admin.site.register(Banka)
admin.site.register(Debit)
admin.site.register(CurrencyUnit)
