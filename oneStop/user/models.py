from django.db import models

# Create your models here.
class User(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('alumni', 'Alumni'),
    )
    username = models.CharField(max_length=50)
    profileCreated = models.BooleanField(default=False)
    profileType = models.CharField(max_length=10, choices=USER_TYPES, blank=True, null=True)
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(max_length=30, blank=True, null=True)
    mobileNumber = models.CharField(max_length=15, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    domain = models.CharField(max_length=50, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    passoutYear = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    currentYear = models.IntegerField(blank=True, null=True)
    areaOfInterest = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username