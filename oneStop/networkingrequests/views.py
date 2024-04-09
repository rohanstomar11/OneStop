from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import NetworkingRequestsSerializer
from .models import NetworkingRequests
from networking.models import Networking

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

class NetworkingStatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, format=None):
        requestId = request.data.get('id')
        try:
            connectionRequest = NetworkingRequests.objects.get(id=requestId)

            connection = Networking.objects.create(
                senderId=connectionRequest.senderId,
                receiverId=connectionRequest.receiverId
            )

            connectionRequest.delete()
        except:
            return Response({"success": "Request Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"success": "Connection Request Approved"}, status=status.HTTP_204_NO_CONTENT)