# mentorship/urls.py

from django.urls import include, path
from rest_framework import routers
from .views import MentorViewSet

router = routers.DefaultRouter()
router.register(r'mentors', MentorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
