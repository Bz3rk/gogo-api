from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import ClientDataSerializer
from .models import ClientDataStore

# Create your views here.
@api_view(['GET', 'POST'])
def ClientLogin(request):
    if request.method == 'GET':
        client = User.objects.all()
        serializer = ClientDataSerializer(client, many=True)
    if request.method == 'POST':
        serializer = ClientDataSerializer(data=request.data)
        
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

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        data = User.objects.create(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
        
        data.save()
    return render(request, 'register.html')