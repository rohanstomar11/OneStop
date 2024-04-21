from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(
    r"mentorshiprequests",
    views.MentorshipRequestsViewSet,
    basename="mentorshiprequests",
)
router.register(
    r"mentorshiprequestsstatus",
    views.MentorshipStatusViewSet,
    basename="mentorshiprequestsstatus",
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
