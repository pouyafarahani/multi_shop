from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model with additional photo field.

    Inherits from Django's built-in AbstractUser model.
    """

    photo = models.ImageField(
        upload_to='user_images/',
        null=True,
        blank=True,
        help_text='User profile picture.'
    )
