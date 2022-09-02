from django.db import models


# Create your models here.
class Employee(models.Model):
    image = models.ImageField(
        null=True,
        blan=True,
        upload_to="profiles"
    )

