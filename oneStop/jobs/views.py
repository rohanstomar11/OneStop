from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Job, SavedJob
from .serializers import JobSerializer, SavedJobSerializer

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username)

    def get_queryset(self):
        queryset = Job.objects.all().order_by('id')
        receiverIdParam = self.request.query_params.get('id', None)

        if receiverIdParam:
            queryset = queryset.filter(id=receiverIdParam)

        return queryset

    @action(detail=True, methods=['post'], url_path='save', url_name='save')
    def save_job(self, request, pk=None):
        job = self.get_object()
        saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=job)
        if created:
            return Response({'message': 'Job saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Job already saved'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='count', url_name='count')
    def get_job_count(self, request):
        count = Job.objects.count()
        return Response({'job_count': count}, status=status.HTTP_200_OK)
