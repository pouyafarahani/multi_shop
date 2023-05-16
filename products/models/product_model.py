from ckeditor.fields import RichTextField
from .category import *


class ProductModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    description = RichTextField()
    short_description = RichTextField(blank=True)

    image = models.ImageField(upload_to='cover_products/')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    color = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
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
