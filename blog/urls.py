from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('notes',views.NotesView.as_view()),
    path('notes/<int:notes_id>/',csrf_exempt(views.NotesDetailView.as_view())),
]