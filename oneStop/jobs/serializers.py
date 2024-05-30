from rest_framework import serializers
from .models import Job, SavedJob

class JobSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['created_by']


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = '__all__'


