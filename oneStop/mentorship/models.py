# mentorship/models.py

from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=200, blank=True)
    education = models.CharField(max_length=200, blank=True)
    experience = models.TextField(blank=True)
    availability = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    areas_of_interest = models.CharField(max_length=200, blank=True)
    languages_spoken = models.CharField(max_length=100, blank=True)
    social_links = models.TextField(blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    feedback = models.TextField(blank=True)
    privacy_settings = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username
