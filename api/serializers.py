from rest_framework import serializers
from .models import *
class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signin
        fields = ('id','username','password')

class Forgot_passwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forgot_password
        fields = ('id','username','email')

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = ('id','otp')

class ConfirmpasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmpassword
        fields = ('id','newpassword','confirmpassword')


                