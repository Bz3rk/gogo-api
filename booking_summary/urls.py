from django.urls import path
from .views import BookingReceipt, create_booking


urlpatterns = [
    path('bookings/create', create_booking, name ='bookings-create'),
    path('bookings/<int:pk>', BookingReceipt, name = 'bookings-receipt'),
]