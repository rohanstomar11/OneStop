from rest_framework import serializers

from .models import MentorshipRequests


class MentorshipRequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MentorshipRequests
        fields = ("id", "studentId", "mentorId")
