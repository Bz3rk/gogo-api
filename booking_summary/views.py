from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import BookingSummary
from .serializers import BookingSummarySerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrAdminOrReadOnly

#from geopy.distance import geodesic

from rest_framework.views import APIView
#from geopy.distance import great_circle


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BookingSummary(request,*args, **kwargs):
    if request.method == 'POST':
        serializer = BookingSummarySerializer(data=request.data)
        if serializer.is_valid():
            pickup_long = float(request.data.get('pickup_long'))
            pickup_lat = float(request.data.get('pickup_lat'))
            dest_long = float(request.data.get('dest_long'))
            dest_lat = float(request.data.get('dest_lat'))
            no_of_passengers = int(request.data.get('no_of_passengers'))


            pickup_location = (pickup_long, pickup_lat)
            destination_location = (dest_long, dest_lat)
            distance = geodesic(pickup_location, destination_location).km
            print(distance)

            base_price = 500
            price = round(base_price * distance * no_of_passengers)
            serializer.save(
                pickup_long=pickup_long,
                pickup_lat=pickup_lat,
                dest_long=dest_long,
                dest_lat=dest_lat,
                no_of_passengers=no_of_passengers,
                distance=distance,
                price=price
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class BookingSummary(APIView):
#     def post(self, request):
#         serializer = BookingSummarySerializer(data=request.data)

#         if serializer.is_valid():
#             # Assuming you're sending the required data in the request body.
#             # You can access it using serializer.validated_data
#             pickup_long = serializer.validated_data.get('pickup_long')
#             pickup_lat = serializer.validated_data.get('pickup_lat')
#             dest_long = serializer.validated_data.get('dest_long')
#             dest_lat = serializer.validated_data.get('dest_lat')
#             no_of_passengers = serializer.validated_data.get('no_of_passengers')

#             try:
#                 # Convert coordinates to tuples
#                 pickup_coords = (pickup_lat, pickup_long)
#                 dest_coords = (dest_lat, dest_long)
                
#                 # Calculate distance
#                 distance = great_circle(pickup_coords, dest_coords).km

#                 # Assuming you've calculated the distance, now calculate the price
#                 base_price = 500
#                 price = round(base_price * distance * no_of_passengers)

#                 # Set the calculated values to the serializer
#                 serializer.validated_data['distance'] = distance
#                 serializer.validated_data['price'] = price

#                 # Create a new instance of BookingSummary
#                 booking_summary = BookingSummary.objects.create(
#                     user=request.user,  # Assuming you have user authentication
#                     user_location=serializer.validated_data.get('user_location'),
#                     destination=serializer.validated_data.get('destination'),
#                     two_way=serializer.validated_data.get('two_way'),
#                     no_of_passengers=no_of_passengers,
#                     pickup_long=pickup_long,
#                     pickup_lat=pickup_lat,
#                     dest_long=dest_long,
#                     dest_lat=dest_lat,
#                     distance=distance,
#                     price=price
#                 )

#                 return Response({'distance': distance, 'price': int(price)})

#             except Exception as e:
#                 return Response({'error': str(e)}, status=400)
#         else:
#             return Response(serializer.errors, status=400)





@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAuthorOrAdminOrReadOnly])
def BookingReceipt(request, pk):
    if request.method == 'GET':
        data = BookingSummary.objects.get(pk=pk)
        serializer = BookingSummarySerializers(data)
    return Response(serializer.data, status=status.HTTP_200_OK)

