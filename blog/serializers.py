from django.db.models import fields
from rest_framework import serializers

from blog.models import NotesModel

class NoteSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=NotesModel
        fields='__all__'