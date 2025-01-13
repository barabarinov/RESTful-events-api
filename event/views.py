from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateTimeFilter
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Event
from .permissions import IsEventOrganizerOrReadOnly
from .serializers import EventSerializer
from .utils import send_event_registration_email


class EventFilter(FilterSet):
    datetime_after = DateTimeFilter(field_name="datetime", lookup_expr="gte")
    datetime_before = DateTimeFilter(field_name="datetime", lookup_expr="lte")

    class Meta:
        model = Event
        fields = ["location", "organizer", "datetime"]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-datetime")
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEventOrganizerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = EventFilter
    search_fields = ["title", "description"]
    ordering_fields = ["datetime", "title"]
    ordering = ["-datetime"]

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
        send_event_registration_email(request.user, event)
        return Response(
            {"detail": "Successfully registered for the event."},
            status=status.HTTP_200_OK,
        )
