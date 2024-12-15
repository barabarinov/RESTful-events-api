from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Event
from .permissions import IsEventOrganizerOrReadOnly
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-datetime")
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEventOrganizerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @swagger_auto_schema(
        operation_description="Register the authenticated user for a specific event.",
        responses={
            200: openapi.Response("Successfully registered for the event."),
            400: openapi.Response("You are already registered for this event."),
        },
    )

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        if request.user in event.guests.all():
            return Response(
                {"detail": "You are already registered for this event."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        event.guests.add(request.user)
        return Response(
            {"detail": "Successfully registered for the event."},
            status=status.HTTP_200_OK,
        )
