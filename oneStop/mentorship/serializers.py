from rest_framework import serializers
from .models import Mentor


class MentorSerializer(serializers.ModelSerializer):
    # Define fields explicitly with custom attributes if needed
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            "id",
            "user",
            "bio",
            "skills",
            "education",
            "experience",
            "availability",
            "location",
            "areas_of_interest",
            "languages_spoken",
            "social_links",
            "average_rating",
            "mentoring_style",
            "feedback",
            "privacy_settings",
        )
