from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet)

app_name = "event"

urlpatterns = [
    path("", include(router.urls)),
]
