from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Feedback(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)