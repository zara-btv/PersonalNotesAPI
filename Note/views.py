
from rest_framework import generics
from Note.permissions import CheckOwnership
from Note.pagination import LargeResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from Note.models import NotePad
from Note.serializer import NotePadSerializer



class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotePadSerializer
    permission_classes = [IsAuthenticated,CheckOwnership]
    def get_queryset(self):
        return NotePad.objects.filter(owner=self.request.user)
    lookup_field = "id"



class NoteListCreateAPIView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NotePadSerializer
    pagination_class = LargeResultsSetPagination
    def get_queryset(self):
        user=self.request.user
        queryset=NotePad.objects.filter(owner_id=user.id)
        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
