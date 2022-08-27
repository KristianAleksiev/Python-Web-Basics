from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=40)


class Employee2(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=40)


class Employee3(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=40)
