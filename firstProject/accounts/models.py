from django.db import models

# Create your models here.
class Customer(models.Model):
    displayName = models.CharField(max_length=264)
    account = models.CharField(max_length=264)
    password = models.CharField(max_length=264)
    
    def __str__(self):
        return str(self.displayName)
    
