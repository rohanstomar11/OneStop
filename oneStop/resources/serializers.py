from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    # Define the uploaded_by field explicitly
    uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Resource
        fields = '__all__'
