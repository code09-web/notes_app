from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from note.models import NotesModel
from rest_framework import generics
from .serializers import NotesSerializer
from rest_framework import permissions
from note.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

