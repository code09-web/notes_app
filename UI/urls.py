from django.urls import path
from django.views.decorators import csrf
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('home',csrf_exempt(notes_page)),
    path('login',csrf_exempt(login)),
    path('create',csrf_exempt(create_notes)),
    path('singup',csrf_exempt(singup)),
    path('details',csrf_exempt(details))
]
