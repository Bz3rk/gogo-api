from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import DataSerializer, ClientRegistrationSerializer, DriverRegistrationSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def ClientLogin(request):
    if request.method == 'GET':
        client = User.objects.all()
        serializer = DataSerializer(client, many=True)
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

    #username = request.data.get('username')
    user = User.objects.get(username=request.user)
    if user.DoesNotExist():
        pass
    
    token = Token.objects.get_or_create(user=user)
    print(request.data.get('username'))
    return Response({'userData': serializer.data, 'token': token[0].key}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def DriverLogin(request):
    if request.method == 'GET':
        client = User.objects.all()
        serializer = DataSerializer(client, many=True)
    if request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

    #username = request.data.get('username')
    user = User.objects.get(username=request.user)
    if user.DoesNotExist():
        pass
    
    token = Token.objects.get_or_create(user=user)
    print(request.data.get('username'))
    return Response({'userData': serializer.data, 'token': token[0].key}, status=status.HTTP_200_OK)


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
        
    return render(request, 'login.html')

@api_view(['POST', 'GET'])
def ClientRegister(request):
    if request.method == 'POST':
        serializer = ClientRegistrationSerializer(data = request.data)
        serializer.save()

    if request.method == 'GET':
        form = User.objects.all()
        serializer = ClientRegistrationSerializer(form, many=True)
    
    user = User.objects.get(username=request.user)
    token = Token.objects.get_or_create(user=user)
    return Response({'userData': serializer.data, 'token':token[0].key}, status=status.HTTP_201_CREATED)

@api_view(['POST', 'GET'])
def DriverRegister(request):
    if request.method == 'POST':
        serializer = DriverRegistrationSerializer(data = request.data)
        serializer.save()

    if request.method == 'GET':
        form = User.objects.all()
        serializer = DriverRegistrationSerializer(form, many=True)
    
    user = User.objects.get(username=request.user)
    token = Token.objects.get_or_create(user=user)
    return Response({'userData': serializer.data, 'token':token[0].key}, status=status.HTTP_201_CREATED)