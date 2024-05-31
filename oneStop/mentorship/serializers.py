# mentorship/serializers.py

from rest_framework import serializers
from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('id', 'user', 'company', 'bio', 'skills', 'education', 'experience', 'availability', 'location', 'areas_of_interest', 'languages_spoken', 'social_links', 'average_rating', 'feedback', 'privacy_settings')
