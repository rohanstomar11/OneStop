from django.urls import path
from authapp.views import RegisterViewSet

urlpatterns = [
    path('register/', RegisterViewSet.as_view(), name='authapp_register'),
]