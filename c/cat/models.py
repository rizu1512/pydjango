from django.db import models

# Create your models here.

class RedCat(models.Model):
    name = models.CharField(max_length=244)
    age = models.IntegerField()
    