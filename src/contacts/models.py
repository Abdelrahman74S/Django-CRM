from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return self.email
