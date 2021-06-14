from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Favourite(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    bookname = models.IntegerField(null=True, blank=True)
    writer = models.CharField(max_length=255, blank=True, null=True)
    published = models.DateField(auto_now_add=False, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


