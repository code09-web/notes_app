from typing import Generic
from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
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
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer


@api_view(['GET'])
def user(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user })


# ----------------------------- login view---------------------------------------------------------------

# @api_view(['POST'])
# @permission_classes([AllowAny])
# @renderer_classes(TemplateHTMLRenderer)

# @ensure_csrf_cookie
# def login_view(request):
#     User=get_user_model()
#     username=request.data.get('username')
#     password=request.data.get('password')
#     response=Response()
#     if(username is None) or (password is None):
#         raise exceptions.AuthenticationFailed(
#             'username and password required'
#         )
    
#     user=User.objects.filter(username=username).first()
#     if(user is None):
#         raise exceptions.AuthenticationFailed('user not found')
#     if(not user.check_password(password)):
#         raise exceptions.AuthenticationFailed('wrong password')
    
#     serialzied_user=UserSerializer(user).data
#     access_token=generate_access_token(user)
#     refresh_token=generate_refresh_token(user)
#     response.set_cookie(key='refreshtoken',value=refresh_token,httponly=True)
#     response.data={
#         'access_token':access_token,
#         'user':serialzied_user,
#     }
#     return response


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


#  ...........................login using apiview .....................................
class UserLoginView(GenericAPIView):
    permission_classes=[AllowAny]
    def post(self ,request,format=None):
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

# ...................... Refrence token ..............................
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):
    User = get_user_model()
    refresh_token = request.COOKIES.get('refreshtoken')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')

    user = User.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')


    access_token = generate_access_token(user)
    return Response({'access_token': access_token})