from django.urls import path
from .views import BookingReceipt, BookingSummary


urlpatterns = [
    path('bookings/create', BookingSummary, name ='bookings-create'),
    path('bookings/<int:pk>', BookingReceipt, name = 'bookings-receipt'),
]