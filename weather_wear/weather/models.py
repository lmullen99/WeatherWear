from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favcities", null=True)
    name = models.CharField(max_length=25, unique = True)
    # make sure name is unique here

    def __str__(self): #show the actual city name on the dashboard]
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'