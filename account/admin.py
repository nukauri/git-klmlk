from django.contrib import admin

# Register your models here.

from .models import Supplier, AccountType,DocumentGroup, DocumentType, Project, Account

admin.site.register(Supplier)
admin.site.register(AccountType)
admin.site.register(DocumentType)
admin.site.register(DocumentGroup)
admin.site.register(Project)
admin.site.register(Account)
