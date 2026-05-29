
from Note.models import NotePad
from rest_framework import serializers


class NotePadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotePad
        fields="__all__"
