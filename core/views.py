from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Event, Alert
from .serializers import EventSerializer, AlertSerializer
from .permissions import IsAdminOrReadOnly

# Allowed values
VALID_SEVERITIES = {"Low", "Medium", "High", "Critical"}
VALID_STATUSES = {"Open", "Acknowledged", "Resolved"}


# -----------------------------
# Event creation API
# -----------------------------
class EventCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer


# -----------------------------
# List / Filter Alerts API
# -----------------------------
class AlertListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer

    def get_queryset(self):
        filters = {}

        if severity := self.request.query_params.get("severity"):
            severity = severity.title()
            if severity in VALID_SEVERITIES:
                filters["event__severity"] = severity

        if status := self.request.query_params.get("status"):
            status = status.title()
            if status in VALID_STATUSES:
                filters["status"] = status

        return Alert.objects.select_related("event").filter(**filters)


# -----------------------------
# Update Alert status (Admin only)
# -----------------------------
class AlertUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
