from django.db import models

# Create your models here.

class Destination(models.Model):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)
