from django.db import models
from django.contrib.auth import get_user_model


class ContactModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject
