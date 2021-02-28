from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.



class Mobile(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Mobile name"))
    brand = models.CharField(max_length=50, verbose_name=_("Brand"))
    price = models.DecimalField(decimal_places=2,max_digits=10 , verbose_name=_("Price"))
    #location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
