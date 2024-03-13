from django.contrib.auth.models import User
from django.db import models

from area import models as area_models
from accomodation import models as accomodation_models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True,null=True)
    contact = models.CharField(max_length=35,blank=True,null=True)
    phoneNumber = models.CharField(max_length=20,blank=True,null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name
    
class AccountType(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'AccountTypes'

    def __str__(self):
        return self.name    
    

class DocumentGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'DocumentGroups'

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(max_length=255)
    accountType =  models.ForeignKey(AccountType,related_name='documentTypes',on_delete=models.CASCADE)

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



class Account(models.Model):
    documentGroup =  models.ForeignKey(DocumentGroup,related_name='accounts',on_delete=models.CASCADE)
    documentType = models.ForeignKey(DocumentType,related_name='accounts',on_delete=models.CASCADE)
    documentDate = models.DateField()
    documentNo = models.CharField(max_length=30)
    description = models.CharField(max_length=255,blank=True,null=True)
    price = models.FloatField()
    area = models.ForeignKey(area_models.Area,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    accomodation = models.ForeignKey(accomodation_models.Accomodation,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    supplier = models.ForeignKey(Supplier,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    project = models.ForeignKey(Project,related_name='accounts',on_delete=models.CASCADE,blank=True,null=True)
    documentImage = models.ImageField(upload_to='item_images',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='accounts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

# Create your models here.
