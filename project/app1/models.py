from sre_constants import MAX_UNTIL
from sys import maxsize
from django.db import models

# Create your models here.

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class Employee(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER, default="")
    image = models.ImageField("/")
    datestamp = models.DateField()

    def __str__(self) -> str:
        return self.first_name

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=250)