from django.db import models
# import uuid
from django.contrib.auth.models import User

# Create your models here.

boolChoice = (
        ("M","Male"),("F","Female")
        )
class MusicandBand1(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    gender = models.CharField(max_length = 1,choices=boolChoice,null=True,blank=True)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/',null=True,blank=True)  
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class Movieandseries(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    gender = models.CharField(max_length = 1,choices=boolChoice,null=True,blank=True)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/',null=True,blank=True)  
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class sports(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    gender = models.CharField(max_length = 1,choices=boolChoice,null=True,blank=True)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/',null=True,blank=True)  
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Dripdoodle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Abstract(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Comics(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Sanskriti(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)