from django.db import models
from django.contrib.auth.models import AbstractUser






from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    favorite_number = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username
