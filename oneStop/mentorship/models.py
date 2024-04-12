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
    privacy_settings = models.TextField(
        blank=True
    )  # Example: JSON field for flexible privacy settings
    # Add any other fields you want to include for the mentor

    def __str__(self):
        return (
            self.user.get_full_name()
            if self.user.get_full_name()
            else self.user.username
        )


class Review(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name="reviews")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, choices=[(i, i) for i in range(1, 6)])
    # You can add additional fields like comments, date, etc. if needed

    class Meta:
        unique_together = (
            "mentor",
            "student",
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_mentor_rating()

    def update_mentor_rating(self):
        reviews = self.mentor.reviews.all()
        total_rating = sum([review.rating for review in reviews])
        avg_rating = total_rating / reviews.count() if reviews.count() > 0 else 0
        self.mentor.rating = avg_rating
        self.mentor.save()
