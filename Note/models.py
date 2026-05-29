from django.db import models
from User.models import CustomUser



class NotePad(models.Model):
    subject = models.CharField(max_length=100)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notes")
    def __str__(self):
        return self.subject