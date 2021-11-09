from django.urls import include, path
from note import views


urlpatterns = [
    # code omitted for brevity
    path('notes/', views.NotesList.as_view()),
    path('notes/<int:pk>/', views.NotesDetail.as_view()),
]