from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    subject=models.TextField(max_length=1000)
    desc = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
      return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=122)
    mobile = models.IntegerField(max_length=12)
    special = models.CharField(max_length=122)

    def __str__(self):
       return self.name


class Patient(models.Model):
    name = models.CharField(max_length=122)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(max_length=12)
    address = models.CharField(max_length=300)
   

    def __str__(self):
       return self.name
