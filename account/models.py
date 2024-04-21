from django.contrib.auth.models import User
from django.db import models

from area import models as area_models
from accomodation import models as accomodation_models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    isCustomer = models.BooleanField(blank=True,null=True)
    isSupplier = models.BooleanField(blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    contact = models.CharField(max_length=35,blank=True,null=True)
    phoneNumber = models.CharField(max_length=20,blank=True,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name
    
class Debit(models.Model):
    supplier = models.ForeignKey(Supplier,related_name='debits',on_delete=models.CASCADE)
    invoiceDate = models.DateField(blank=True,null=True)
    invoicePrice = models.FloatField(blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    paymentTerm = models.IntegerField(blank=True,null=True)
    area = models.ForeignKey(area_models.Area,related_name='debits',on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering = ('supplier',)
        verbose_name_plural = 'Debits'

    def __str__(self):
        return self.supplier
    

    

class DocumentGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'DocumentGroups'

    def __str__(self):
        return self.name


class DocumentType(models.Model):
            class AccountTypeChoices(models.TextChoices):
             Gelir="GL"
             Gider = "GD"

            name = models.CharField(max_length=255)
            accountType =  models.CharField(max_length =2,choices=AccountTypeChoices.choices)

            class Meta:
                ordering = ('name',)
                verbose_name_plural = 'DocumentTypes'

            def __str__(self):
                return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

class PayType(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'PayType'

    def __str__(self):
        return self.name
    
class Banka(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Banka'

    def __str__(self):
        return self.name
    
class CurrencyUnit(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'CurrencyUnits'

    def __str__(self):
        return self.name
    


class Account(models.Model):
    documentType = models.ForeignKey(DocumentType,related_name='accounts',on_delete=models.CASCADE)
    payType = models.ForeignKey(PayType,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    banka = models.ForeignKey(Banka,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    documentDate = models.DateField()
    description = models.CharField(max_length=255,blank=True,null=True)
    price = models.FloatField()
    currencyUnit = models.ForeignKey(CurrencyUnit,related_name='accounts',on_delete=models.CASCADE)
    area = models.ForeignKey(area_models.Area,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    supplier = models.ForeignKey(Supplier,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    documentImage = models.ImageField(upload_to='item_images',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='accounts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

# Create your models here.
