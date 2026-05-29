from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from User.permissions import UniqueApiPermission
from Note.pagination import LargeResultsSetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from Note.models import NotePad
from User.serializer import RegisterUserSerializer
from Note.serializer import NotePadSerializer
from rest_framework.permissions import AllowAny

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer_class = RegisterUserSerializer(data=request.data)
        if serializer_class.is_valid():
            user=serializer_class.save()
            user.set_password(request.data['password'])
            user.save()
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result":{"user_id":user.id}},status=status.HTTP_200_OK)



class ChangGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotePadSerializer
    permission_classes = [UniqueApiPermission,IsAuthenticated]
    queryset = NotePad.objects.all()
    lookup_field = "id"

class CreateGenericAPIView(generics.ListCreateAPIView):
    pagination_class = [LargeResultsSetPagination]
    permission_classes = [UniqueApiPermission,IsAuthenticated]
    serializer_class = NotePadSerializer
    queryset = NotePad.objects.all()

