from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

from .category import Category


class ProductModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # $0123456789.42
    description = RichTextField()
    shor_description = RichTextField(blank=True)
    size_choices = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    sizes = models.CharField(max_length=2, choices=size_choices)
    color = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    datetime_create = models.DateTimeField(default=timezone.now)
    datetime_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
