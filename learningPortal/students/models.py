from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30)
    age = models.IntegerField()
    location = models.CharField(max_length=20)



    def __str__(self):
        return self.name