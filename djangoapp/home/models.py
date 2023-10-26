from typing import Any
from django.db import models

# Create your models here.
class Boutique(models.Model):
    location= models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    prouduct= models.CharField(max_length=200,default="null")
    def __str__(self):
        return self.name
   