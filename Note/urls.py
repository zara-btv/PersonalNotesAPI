
from django.urls import path,include

from Note.views import NoteListCreateAPIView,NoteDetailAPIView

urlpatterns = [
    path("<int:id>/", NoteDetailAPIView.as_view(), name="note-detail"),
    path("", NoteListCreateAPIView.as_view(), name="note-list-create"),
]
