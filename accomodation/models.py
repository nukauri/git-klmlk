from django.contrib.auth.models import User
from django.db import models
from area import models as area_models



# Create your models here.

class Accomodation(models.Model):
    area =  models.ForeignKey(area_models.Area,related_name='accomodations',on_delete=models.CASCADE)
    address = models.ForeignKey(area_models.Address,related_name='accomodations',on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField(blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    tlfNo = models.CharField(max_length=30,blank=True,null=True)
    plaka = models.CharField(max_length=30,blank=True,null=True)
    status = models.BooleanField(blank=True,null=True)
    is_paid = models.BooleanField(blank=True,null=True)
    is_closed = models.BooleanField(blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='accomodations',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Accomodations'

    def __str__(self):
        return self.name
