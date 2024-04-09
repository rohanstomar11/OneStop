from rest_framework import serializers

from .models import Networking

class NetworkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Networking
        fields = ('id', 'senderId', 'receiverId')