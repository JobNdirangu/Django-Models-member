from django.db import models

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    secondname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
