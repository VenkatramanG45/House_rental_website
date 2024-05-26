from django.db import models
from django.utils import timezone
# Create your models here.
# rental/models.py
from django.contrib.auth.models import User
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='property_images/')
    #house = models.CharField(max_length=100) 
    # Add more fields as needed

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null= True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    
    def __str__(self):
        return f'Booking by {self.full_name} for {self.property.title}'

