from django.urls import path
from .views import *

urlpatterns = [
    path('', SigninView.as_view()),
    path('signin', SigninView.as_view()),
    path('forgetpass',Forgot_passwordView.as_view()),
    path('otp', OtpView.as_view()),
    path('confirmpass', ConfirmpasswordView.as_view()),
]