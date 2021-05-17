from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics

from .serializers import RegistrationUserSerializer, LoginSerializer
from .models import UserModels

from django.urls import reverse

from .utils import Util


class RegistrationUserAPIView(generics.GenericAPIView):
    serializer_class = RegistrationUserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = UserModels.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        relativeLink = reverse('users:email-verify')
        absurl = 'http://localhost:3000/auth/activate/' + str(token)
        email_body = 'Hi ' + user.first_name + \
                     ' Use the link below to verify your email \n This token is available only for 10 minutes \n' + \
                     absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



