from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField()
    area = models.CharField()
    buildtime = models.DateTimeField('date published')


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=10)
    sex = models.CharField()
    school = models.ForeignKey(School,on_delete=None)