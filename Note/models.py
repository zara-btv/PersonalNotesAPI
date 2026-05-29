from django.db import models
from django.conf import settings
from datetime import datetime
from User.models import *


class NotePad(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    subject=models.CharField(max_length=100, blank=True,null=True)
    note = models.TextField(max_length=500,blank=True,null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)