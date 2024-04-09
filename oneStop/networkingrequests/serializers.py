from rest_framework import serializers

from .models import NetworkingRequests

class NetworkingRequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkingRequests
        fields = ('id', 'senderId', 'receiverId')