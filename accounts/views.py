import json

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (UserSerializer,
                          PasswordForgotSerializer,
                          PasswordForgotConfirmSerializer,
                          RegionSerializer)
from .permissions import IsTokenValid
from .utils import send_email
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate activation token
            token = get_random_string(length=32)
            user.activation_token = token
            user.save()

            # Send activation email
            url_path = f"{request.scheme}://{request.get_host()}"
            send_email(user.email, token, domain=url_path)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Activating users after they request activation link
#test cicd
#test1 aws
class ActivationView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            user = User.objects.get(activation_token=token)
            user.is_active = True
            user.activation_token = None
            user.save()
            # needs to be redirected to login page after the frontend is ready
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Invalid activation token.'}, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-timestamp')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        data = serializer.data
        del data['password']
        return Response(data)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=openapi.Schema(
       type=openapi.TYPE_OBJECT,
       properties={
         'refresh_token':openapi.Schema(type=openapi.TYPE_STRING),
       }, 
       required=['refresh_token'],
    ))
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Logout failed'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordForgotView(generics.CreateAPIView):
    serializer_class = PasswordForgotSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email)

        if user.exists():
            # Generate a reset token using SimpleJWT
            user = user.first()
            refresh = RefreshToken.for_user(user)
            reset_token = str(refresh)

            # Send the link with reset_token to the user (e.g., via email)
            url_path = f"{request.scheme}://{request.get_host()}"
            send_email(user.email, reset_token, domain=url_path, email_type="forgot_pass")

            return Response({'detail': 'Password reset token sent successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User with this email address does not exist.'}, status=status.HTTP_404_NOT_FOUND)


class PasswordForgotConfirmView(generics.CreateAPIView):
    serializer_class = PasswordForgotConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_token = self.kwargs.get("reset_token")
        new_password = serializer.validated_data['new_password']

        try:
            # Attempt to verify the reset token
            refresh = RefreshToken(reset_token)
            user_id = refresh['user_id']
        except Exception as e:
            return Response({'detail': 'Invalid reset token.'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the user by user_id and update the password
        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()

        # redirect to login page
        return Response({'detail': 'Password reset successfully.'}, status=status.HTTP_200_OK)


class GetCountryListView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        with open('regions.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class GetStateListView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        with open('regions.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        country_name = kwargs["country_name"]
        states = next((item['states'] for item in data if item.get('name') == country_name), None)

        if len(states) == 0:
            states = [{"name": country_name}]
        serializer = self.serializer_class(data=states, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class GetCityListView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        with open('regions.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        country_name = kwargs["country_name"]
        state_name = kwargs["state_name"]
        states = next((item['states'] for item in data if item.get('name') == country_name), None)
        cities = next((item['cities'] for item in states if item.get('name') == state_name), None)   
        
        if states == [] and (cities == [] or cities == None):
            states = [{"name": country_name}]
            cities = [{"name": country_name}]

        if states != [] and cities == []:
            cities = [{"name": state_name}]

        serializer = self.serializer_class(data=cities, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
