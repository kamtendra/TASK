from django.db import models
from django.core.validators import RegexValidator
import string
import random

# def generate_unique_code():
#     length=6
#     while True:
#         code =''.join(random.choices(string.ascii_uppercase,k=length))
#         if Room.objects.filter(code=code).count()==0:
#             break
#     return code     

class Signin(models.Model):
    username=models.CharField(null=False,blank=False,unique=True,max_length=10)
    password=models.CharField(null=False,blank=False,max_length=10)

class Forgot_password(models.Model):
    username=models.CharField(null=False,blank=False,unique=True,max_length=10
    )    
    email=models.EmailField(null=False,blank=False,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False) # Validators should be a list

class Otp(models.Model):
    otp=models.IntegerField(null=False,blank=False)

class Confirmpassword(models.Model):
    newpassword = models.CharField(null=False,blank=False,max_length=10)
    confirmpassword = models.CharField(null=False,blank=False,max_length=10)       

