from rest_framework import serializers
from .models import Event, Alert

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = "__all__"

    def create(self, validated_data):
        event = super().create(validated_data)
        if event.severity in ["High", "Critical"]: # Auto create alert
            Alert.objects.create(event=event)
        return event



class AlertSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    class Meta:
        model = Alert 
        fields = "__all__"