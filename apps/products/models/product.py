from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

from .product_category import Category


class ProductModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    title = models.CharField(max_length=150)
    description = RichTextField()
    short_description = RichTextField(blank=True)
    information = RichTextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    color = models.CharField(max_length=50)
    size_choices = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    sizes = models.CharField(max_length=2, choices=size_choices)

    active = models.BooleanField(default=True)
    featured_products = models.BooleanField(default=False)

    datetime_edit = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_Detail', args=[self.pk])
