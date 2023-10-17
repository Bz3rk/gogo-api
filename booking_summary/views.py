from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import BookingSummary
from .serializers import BookingSummarySerializer
#from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from drf_spectacular.utils import extend_schema

from rest_framework.permissions import IsAuthenticated
#from .permissions import IsAuthorToViewReceipt

from geopy.distance import geodesic



@extend_schema(request = BookingSummarySerializer,  responses = BookingSummarySerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    def calculate_total_price(base_price, distance, passengers):
        # function calculate total price based on base price, distance, and number of passengers
        return round(base_price * distance * passengers)

    if request.method == 'POST':
        data = request.data
        # checks if the required fields are inputted
        
                
        longitude = data.get('pickup_long')
        latitude = data.get('pickup_lat')
        destination_longitude = data.get('dest_long')
        destination_latitude = data.get('dest_lat')
        passengers = data.get('no_of_passengers')   
        two_way = data.get('two_way')
        user_location = data.get('user_location')
        destination = data.get('destination')

       # checkes if each field is provided
        required_fields = ['user_location','destination','pickup_long', 'pickup_lat', 'dest_long', 'dest_lat', 'no_of_passengers', 'two_way']

        for field in required_fields:
            if field not in data:
                return Response({'message': f'{field.replace("_", " ").capitalize()} is required'}, status=status.HTTP_400_BAD_REQUEST)

        if longitude is not None and latitude is not None and passengers is not None and destination_latitude is not None and destination_latitude is not None:
            try:
                pickup_location = (float(latitude), float(longitude))
                destination = (float(destination_latitude), float(destination_longitude))
            except ValueError:
                return Response({'message': 'Invalid longitude or latitude format'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                cal_distance = geodesic(pickup_location, destination).kilometers
                distance = round(cal_distance, 2)
            except Exception as e:
                return Response({'message': f'Error calculating distance: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

            base_price = 500  # Setting a default base price of 500


            if two_way is True:
                price = (calculate_total_price(base_price, distance, passengers) * 2)
            else:
                price = calculate_total_price(base_price, distance, passengers)
                
            print(price)
            print(distance)

            user = request.user 
            serializer = BookingSummarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(
                    distance=distance,
                    price=price,
                    user = user
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'user_location, destination, two_way, no_of_passengers, pickup_long, pickup_lat, dest_long, dest_lat are required'}, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    return Response({'message': 'Method not allowed. Use POST to create a booking.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
 









@extend_schema(request = BookingSummarySerializer, responses = BookingSummarySerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def BookingReceipt(request, user_id):
    if request.method == 'GET':
        try:
            user = request.user 

            if str(user.id) != user_id:
                return Response({'message': 'Unauthorized access'}, status=status.HTTP_401_UNAUTHORIZED)
            data = user.bookingsummary_set.filter(user_id=user_id).order_by('-id')
            serializer = BookingSummarySerializer(data=data, many=True)
            if serializer.is_valid():
                data = serializer.data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookingSummary.DoesNotExist:
            return Response({'message': 'Booking Receipt not found'}, status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def BookingReceipt(request, user_id):
#     if request.method == 'GET':
#         try:
#             user = request.user 
#             data = user.BookingSummary_set.filter(user_id=user_id)
#         except BookingSummary.DoesNotExist:
#             return Response({'message': 'Booking Receipt not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookingSummarySerializer(data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
