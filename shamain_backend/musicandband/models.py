from django.db import models
import uuid

# Create your models here.

# class MusicandBand(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=500)
#     price= models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.CharField(max_length=600)
    # images = models.ImageField(upload_to ='uploads/')
    # images = models.ImageField(upload_to='pics')
    
class MusicandBand1(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class Movieandseries(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
class sports(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600)
    
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