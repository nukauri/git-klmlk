from django.contrib import admin

# Register your models here.

from .models import Supplier, AccountType,DocumentGroup, DocumentType, Project, Account,PayType,Document,Banka

admin.site.register(Supplier)
admin.site.register(AccountType)
admin.site.register(DocumentType)
admin.site.register(DocumentGroup)
admin.site.register(Project)
admin.site.register(Account)
admin.site.register(PayType)
admin.site.register(Document)
admin.site.register(Banka)
