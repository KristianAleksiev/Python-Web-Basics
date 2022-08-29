from django.db import models
from django.urls import reverse


# Create your models here.

class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department details: ", kwargs={
            "id": self.id,
        })


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    DATA_SCIENTIST = 2
    DEVOPS_ENGINEER = 5
    FINALLY_FIXED = "YES!!!"

    AMAZON = "AMZN"
    GOOGLE = "GOOGLE"

    first_name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="First name",
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        default="NO NAME",
    )
    job_title = models.IntegerField(

        choices=(
            # (1, "Software developer"),
            # (2, "Data Scientist"),
            # (3, "DevOps"),

            #  Defined outside the model =>
            (SOFTWARE_DEVELOPER, "Software developer"),
            (DATA_SCIENTIST, "Data scientist"),
            (DEVOPS_ENGINEER, "DevOps"),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in [AMAZON, GOOGLE]),
        choices=(
            (AMAZON, "AMAZON"),
            (GOOGLE, "GOOGLE"),
        )
    )

    class Meta:
        ordering = ("company", "first_name",)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Project(models.Model):
    employees = models.ManyToManyField(to=Employee)
    name = models.CharField(
        max_length=30,
    )
    deadline = models.DateField(
        null=True,
        blank=True,

    )


class TestAgain(models.Model):
    name = models.DateField
    second_try = models.CharField(max_length=50, )
