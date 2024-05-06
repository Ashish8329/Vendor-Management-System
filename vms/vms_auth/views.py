from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from vms_auth.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                {"message": "Invalid data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        user = User.objects.get(username=serializer.data["username"])

        return Response(
            {"message": "User registered successfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        refresh = RefreshToken.for_user(user)

        
        if not user:
            return Response(
                {"message": "Invalid username or password", },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {"message": "Login successful", "refresh": str(refresh),'access':str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )
