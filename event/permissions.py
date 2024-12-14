from rest_framework import permissions

from .models import Event


class IsEventOrganizerOrReadOnly(permissions.BasePermission):
    """
    Allows only the organizer of the event to modify or delete it.
    Other users have read-only access.
    """

    def has_object_permission(self, request, view, event: Event) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return event.organizer == request.user
