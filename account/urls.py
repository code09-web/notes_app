from django.urls import include, path

from .views import  user,UserRegisterView,UserLoginView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('user', user, name='user'),
    path('login',UserLoginView.as_view(),name='login'),
    path('register',UserRegisterView.as_view(),name='register')
]