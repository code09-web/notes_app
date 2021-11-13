from django.urls import include, path

from .views import  UserRegisterView,UserLoginView
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    # path('user', user, name='user'),
    path('login',csrf_exempt(UserLoginView.as_view()),name='login_api'),
    path('register',csrf_exempt(UserRegisterView.as_view()),name='register_api'),
]