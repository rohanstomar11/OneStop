from rest_framework import viewsets

from .serializers import MentorSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Mentor


class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by("user")
    serializer_class = MentorSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Mentor.objects.all().order_by("id")

        receiverIdParam = self.request.query_params.get("id", None)

        if receiverIdParam:
            queryset = queryset.filter(receiverId=receiverIdParam)

        return queryset
