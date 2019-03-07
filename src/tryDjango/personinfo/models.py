from django.db import models
from django.urls import reverse


# Create your models here.

class Person(models.Model):
    name        = models.CharField(max_length=200)
    birthdate   = models.DateField()
    fathername  = models.CharField(max_length=200)
    mothername  = models.CharField(max_length=200)
    school      = models.BooleanField()
    college     = models.BooleanField()
    university  = models.BooleanField()


    def get_absolute_url(self):
        return reverse("personinfo:person-detail", kwargs={"id": self.id})
    