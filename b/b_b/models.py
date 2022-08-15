from django.db import models

# Create your models here.
class BB(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=300)