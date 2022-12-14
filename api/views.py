from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import *

class SigninView(generics.ListCreateAPIView):
    queryset=Signin.objects.all()
    serializer_class=SigninSerializer

class Forgot_passwordView(generics.ListCreateAPIView):
    queryset=Forgot_password.objects.all()
    serializer_class=Forgot_passwordSerializer

class OtpView(generics.ListCreateAPIView):
    queryset=Otp.objects.all()
    serializer_class=OtpSerializer    

class ConfirmpasswordView(generics.ListCreateAPIView):
    queryset=Confirmpassword.objects.all()
    serializer_class=ConfirmpasswordSerializer     