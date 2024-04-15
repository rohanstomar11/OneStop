from django.db import models


class MentorshipRequests(models.Model):
    studentId = models.CharField(max_length=10)
    mentorId = models.CharField(max_length=10)

    def __str__(self):
        return self.senderId
