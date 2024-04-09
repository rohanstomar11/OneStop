from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import NetworkingSerializer
from .models import Networking


class NetworkingViewSet(viewsets.ModelViewSet):
    queryset = Networking.objects.all().order_by('id')
    serializer_class = NetworkingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Networking.objects.all().order_by('id')

        receiverIdParam = self.request.query_params.get('id', None)

        if receiverIdParam:
            queryset = queryset.filter(receiverId=receiverIdParam)

        return queryset
