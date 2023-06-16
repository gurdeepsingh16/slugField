from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    slug = AutoSlugField(populate_from ='name',null=True,unique=True)