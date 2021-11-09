from rest_framework import fields, serializers
from .models import NotesModel
class NotesSerializer(serializers.ModelSerializer):
    # post_author_username = serializers.ReadOnlyField(source="post_author.username")
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=NotesModel
        fields=['id','title','body','owner']