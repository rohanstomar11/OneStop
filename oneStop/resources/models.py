from django.db import models

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic Resource'),
        ('career', 'Career Resource'),
        ('general', 'General Resource'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=150)  # Change to CharField
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='unknown')

    def __str__(self):
        return self.title
