from django.contrib.auth import get_user_model

from product import *


class ProductComment(models.Model):
    products = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')

    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)
