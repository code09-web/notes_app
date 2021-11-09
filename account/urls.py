from django.urls import include, path

from .views import  user,login_view,UserRegisterView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('user', user, name='user'),
    path('login',login_view,name='login'),
    path('register',UserRegisterView.as_view(),name='register')
]