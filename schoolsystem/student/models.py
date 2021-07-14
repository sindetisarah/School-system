from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    second_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    
    nationality=models.CharField(max_length=12)
    class_name=models.CharField(max_length=10)

