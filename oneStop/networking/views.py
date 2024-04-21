from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def delete(self, request, format=None):
        try:
            id = self.request.query_params.get('id', None)
            connection = Networking.objects.get(id=id)
            connection.delete()
        except:
            return Response({"success": "Connection Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"success": "Connection Removed!"}, status=status.HTTP_200_OK)