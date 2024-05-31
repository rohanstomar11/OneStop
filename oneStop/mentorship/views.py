# mentorship/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Mentor
from .serializers import MentorSerializer

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all().order_by('user')
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]
