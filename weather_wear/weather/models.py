from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    # make sure name is unique here
    name = models.CharField(max_length=35)


    def __str__(self): #show the actual city name on the dashboard]
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
        unique_together = ('owner', 'name',)

class Outfit(models.Model):
    temp = models.IntegerField(unique = True)
    top = models.CharField(max_length=40)
    bottom = models.CharField(max_length=40)
    outerwear = models.CharField(max_length=40)
    accessories = models.CharField(max_length=50)
    footwear = models.CharField(max_length=40)