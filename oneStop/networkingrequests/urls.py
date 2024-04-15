from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'connectionrequests', views.NetworkingRequestsViewSet, basename='connectionrequests')
router.register(r'connectionrequestsstatus', views.NetworkingStatusViewSet, basename='connectionrequestsstatus')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]