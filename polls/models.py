from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    buildtime = models.DateTimeField('date published')


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=10)
    sex = models.CharField(max_length=10)
    school = models.ForeignKey(School,on_delete=None)