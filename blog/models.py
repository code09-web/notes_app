from django.db import models
from django.contrib.auth.models import User

class NotesModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=220)
    body=models.TextField()

    def __str__(self):
        return self.title