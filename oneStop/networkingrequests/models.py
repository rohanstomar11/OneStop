from django.db import models

# Create your models here.
class NetworkingRequests(models.Model):
    senderId = models.CharField(max_length=10)
    receiverId = models.CharField(max_length=10)
    
    def __str__(self):
        return self.senderId