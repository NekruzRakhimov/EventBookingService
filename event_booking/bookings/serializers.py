from rest_framework import serializers
from .models import Booking
from events.serializers import EventSerializer


class BookingSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'event', 'created_at']


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['event']

    def validate_event(self, event):
        user = self.context['request'].user
        if Booking.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("Вы уже забронировали это мероприятие.")
        return event

    def create(self, validated_data):
        user = self.context['request'].user
        return Booking.objects.create(user=user, **validated_data)
