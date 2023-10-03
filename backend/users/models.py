from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = EmailField(_("email address"), unique=True)
    username = CharField(_("Username"), unique=True, max_length=32)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    