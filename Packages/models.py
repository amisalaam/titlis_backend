from django.db import models

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/packages', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TripPlans(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/trip_plans', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name