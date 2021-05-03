from django.db import models

class Cityy(models.Model):
    name = models.CharField(max_length=20)

class Categories(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.
class Registrationform(models.Model):
    Firstname =models.CharField(max_length=400, null=True, blank=True)
    Lastname =models.CharField(max_length=400, null=True, blank=True)
    Email =models.CharField(max_length=400, null=True, blank=True)
    Phone =models.CharField(max_length=400,null=True, blank=True)
    Address =models.CharField(max_length=400, null=True, blank=True)
    City =models.CharField(max_length=600, blank=True)
    program =models.CharField(max_length=400,null=True, blank=True)

    def __str__(self):
        return self.Firstname

class Newslettersubcriber(models.Model):
    email   =  models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email
