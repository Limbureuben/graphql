from pyexpat import model
from django.db import models
from datetime import date

# Create your models here.

class Registration(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define the id field
    username = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=50, default="")
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
    
class Application(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, default="null")
    email = models.EmailField(max_length=255, default="null")
    region = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=10, default="0625219727")
    application_date = models.DateField(default=date.today, null=True, blank=True)

    
    def __str__(self):
        return self.username
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255, default="null")
    published_date = models.DateField(default=date.today, null=True)
    text = models.TextField()
    
    

class Employment(models.Model):
    job_title = models.CharField(max_length=55, default="")
    employ_status = models.CharField(max_length=255, default="")
    details_month = models.CharField(max_length=255, default="")
    employ_name = models.CharField(max_length=255, default="")
    
    
    def __str__(self):
        return self.employ_status
    

class Weather(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
class Financial(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    passport_path = models.CharField(max_length=200, null=True, blank=True)
    
class Files(models.Model):
    file = models.FileField(upload_to="uploads/", null=True, blank=True)