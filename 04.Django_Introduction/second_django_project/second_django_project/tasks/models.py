from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False,
        unique=True,

    )
    text = models.CharField(
        max_length=50,
    )


class Category(models.Model):
    title = models.CharField(
        max_length=125,
    )
