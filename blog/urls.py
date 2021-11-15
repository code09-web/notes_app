from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('notes',csrf_exempt(views.NotesView.as_view()),name='notes_api'),
    path('notes/<int:notes_id>/',csrf_exempt(views.NotesDetailView.as_view()),name='crud_api'),
]