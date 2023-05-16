from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='cover_products/')
    image2 = models.ImageField(upload_to='cover_products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='cover_products/', null=True, blank=True)
    image4 = models.ImageField(upload_to='cover_products/', null=True, blank=True)
    image5 = models.ImageField(upload_to='cover_products/', null=True, blank=True)

