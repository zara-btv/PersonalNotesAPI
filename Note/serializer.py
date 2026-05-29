
from Note.models import NotePad
from rest_framework import serializers


class NotePadSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotePad
        fields = ['id', 'subject', 'note', 'date', 'owner']
        read_only_fields = ['id', 'date', 'owner']
