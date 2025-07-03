from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate
from .serializers import CustomToken_Serializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):

    def post(self, request):

        new_user = User(username = request.data['username'])

        new_user.set_password(request.data['password'])

        new_user.save()

        return Response("New User Created")

class UserLoginView(APIView):

    def post(self, request):

        user_data = CustomToken_Serializer(data = request.data)

        if user_data.is_valid():
            
            return Response(user_data.validated_data)
        
        else:
 
            return Response(user_data.errors)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Only allow authenticated users

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })
