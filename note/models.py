from django.db import models
from django.contrib.auth.models import User
from django .conf import settings
from django.utils import timezone
class NotesModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    body=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
         return self.title
