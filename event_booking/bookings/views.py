from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer, CreateBookingSerializer

from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer


class MyBookingsListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class CreateBookingView(generics.CreateAPIView):
    serializer_class = CreateBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# -> request -> middleware(auth check) ->  middleware(...) ->  middleware(...) -> MyBookingsListView