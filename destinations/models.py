from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    country = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    location_link = models.URLField()           
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)  # New ImageField

    def __str__(self):
        return self.place_name
