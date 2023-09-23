from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, TextField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    email = EmailField(_("email address"), unique=True)
    username = TextField(_("Username"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email