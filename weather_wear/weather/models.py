from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    # make sure name is unique here
    name = models.CharField(max_length=25, unique = True)


    def __str__(self): #show the actual city name on the dashboard]
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'