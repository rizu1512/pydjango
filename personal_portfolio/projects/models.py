from pydoc import describe
from pyexpat import model
from django.db import models
from matplotlib.pyplot import title
from tables import Description


# Create your models here.

class Project(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='Muhammad Rizwan\Desktop\Django\personal_portfolio\img' , default='download.png')