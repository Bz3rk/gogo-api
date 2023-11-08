from django.urls import path
from .views import bookingReceipt, createBooking, junctionList, priceTableList, bookRide, rideSummary


urlpatterns = [
    path('bookings/create', createBooking, name ='createBooking'),
    path('bookings/<str:user_id>', bookingReceipt, name = 'bookingReceipt'),
    path('book-ride/', bookRide, name='bookRide'),
    path('junction-list/', junctionList, name='junctionList'),
    path('price-table-list/', priceTableList, name='priceTableList'),
    path('ride-summary/<int:ride_id>', rideSummary, name = ' rideSummary'),
]