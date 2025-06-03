from django.urls import path
from .views import MyBookingsListView, CreateBookingView

urlpatterns = [
    path('my/', MyBookingsListView.as_view(), name='my-bookings'),
    path('', CreateBookingView.as_view(), name='create-booking'),
]
