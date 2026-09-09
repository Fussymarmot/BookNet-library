from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # аватар
    bio = models.TextField(blank=True)  # немного о себе

    def __str__(self):
        return f'Профиль {self.user.username}'
