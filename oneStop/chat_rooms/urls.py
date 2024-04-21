from django.urls import path
from . import views

urlpatterns = [
    path("rooms/", views.RoomListCreateAPIView.as_view(), name="room-list-create"),
    path(
        "rooms/<int:pk>/",
        views.RoomRetrieveUpdateDestroyAPIView.as_view(),
        name="room-detail",
    ),
    path(
        "messages/",
        views.MessageListCreateAPIView.as_view(),
        name="message-list-create",
    ),
    path(
        "messages/<int:pk>/",
        views.MessageRetrieveUpdateDestroyAPIView.as_view(),
        name="message-detail",
    ),
]
