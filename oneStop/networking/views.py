from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all().order_by('id')

        email_param = self.request.query_params.get('email', None)

        if email_param:
            queryset = queryset.filter(email=email_param)

        return queryset
