from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
    
    class Meta:
        model = User
        fields = ('id', 'username', 'profileCreated', 'profileType', 'firstName', 'lastName', 'mobileNumber', 'branch', 'domain', 'dateOfBirth', 'passoutYear', 'company', 'currentYear', 'areaOfInterest')