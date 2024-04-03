from django.db import models

# Create your models here.
class Area(models.Model):
        class AreaTypeChoices(models.TextChoices):
             TENTE="T"
             CARAVAN = "C"
             ROOM = "H"
             NOTAREA = "N"

        name = models.CharField(max_length=30)
        capacity = models.IntegerField(blank=True,null=True)
        areaType = models.CharField(max_length =1,choices=AreaTypeChoices.choices)
        

        class Meta:
            ordering = ('name',)
            verbose_name_plural = 'Areas'

        def __str__(self):
            return self.name
    

class Address(models.Model):
    area =  models.ForeignKey(Area,related_name='addresses',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.name
