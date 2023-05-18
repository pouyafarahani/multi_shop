from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cover_category/')

    def __str__(self):
        return self.name
