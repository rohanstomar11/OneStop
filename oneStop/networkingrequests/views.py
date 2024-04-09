from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NetworkingRequestsSerializer
from .models import NetworkingRequests


class NetworkingRequestsViewSet(viewsets.ModelViewSet):
    queryset = NetworkingRequests.objects.all().order_by('id')
    serializer_class = NetworkingRequestsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = NetworkingRequests.objects.all().order_by('id')

        receiverIdParam = self.request.query_params.get('id', None)

        if receiverIdParam:
            queryset = queryset.filter(receiverId=receiverIdParam)

        return queryset
