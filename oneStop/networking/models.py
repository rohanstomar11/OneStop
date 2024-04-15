from django.db import models

class Networking(models.Model):
    senderId = models.CharField(max_length=10)
    receiverId = models.CharField(max_length=10)
    
    def __str__(self):
        return self.senderId