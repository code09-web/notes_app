from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from .auth import generate_access_token, generate_refresh_token
from django.views.decorators.csrf import csrf_protect
import jwt
from django.conf import settings
from rest_framework.generics import GenericAPIView

@api_view(['GET'])
def user(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })


# ----------------------------- login view---------------------------------------------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User=get_user_model()
    username=request.data.get('username')
    password=request.data.get('password')
    response=Response()
    if(username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required'
        )
    
    user=User.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if(not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')
    
    serialzied_user=UserSerializer(user).data
    access_token=generate_access_token(user)
    refresh_token=generate_refresh_token(user)
    response.set_cookie(key='refreshtoken',value=refresh_token,httponly=True)
    response.data={
        'access_token':access_token,
        'user':serialzied_user,
    }
    return response


# .......................................... Registration ................................................
class UserRegisterView(GenericAPIView):
    serializers_classes=RegisterSerializer
    permission_classes=[AllowAny]
    def post(self,request,format=None):
        try:
            serializers=RegisterSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'status':200,'message':'created successfully'})
            else:
                return Response({'status':404,'message':serializers.errors})
        except Exception as e:
            print(e)
            return Response({'status':200,'error':'Somthing went wrong'})


