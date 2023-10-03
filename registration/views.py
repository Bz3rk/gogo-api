from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import DataSerializer, ClientRegistrationSerializer, DriverRegistrationSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def ClientLogin(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"detail": "Not Found..."}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        serializer = DataSerializer(instance=user)
        return Response({'userData': serializer.data, 'token': token.key}, status=status.HTTP_200_OK)
    return Response({})

@api_view(['GET', 'POST'])
def DriverLogin(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
           return Response({"detail": "Not Found..."}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        serializer = DataSerializer(instance=user)
        return Response({'userData': serializer.data, 'token': token.key}, status=status.HTTP_200_OK)
    return Response({})

@api_view(['POST', 'GET'])
def ClientRegister(request):
    if request.method == 'POST':
        serializer = ClientRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            password = make_password(request.data['password'])
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            return Response({'userData': serializer.data, 'token': token.key})
        return Response({'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({})

@api_view(['POST', 'GET'])
def DriverRegister(request):
    if request.method == 'POST':
        serializer = DriverRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            password = make_password(request.data['password'])
            serializer.save(password=password)
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)
            return Response({"userData": serializer.data, "token": token.key})
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response({})

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"success":True})