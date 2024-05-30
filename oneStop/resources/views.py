from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Resource
from .serializers import ResourceSerializer

class ResourcesViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all().order_by('uploaded_at')
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user.username)  # Save username directly

    def get_queryset(self):
        queryset = Resource.objects.all().order_by('uploaded_at')
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset
