from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
import datetime 
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class HelloWorld(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message":"Hello World"})





'''def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_meal')  # Redirect to 'list' page after successful login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html') '''


def generate_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        print("Hello")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Ok")
            token = generate_jwt_token(user)
            return Response({'token': token})
        else:
            
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

'''class LoginView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        return Response({"success":"success"})
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message":"login successfull"})
        else :
            return Response({"message":"Not found"})'''


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello_world(request):
    return Response({"message":"Hello world"})