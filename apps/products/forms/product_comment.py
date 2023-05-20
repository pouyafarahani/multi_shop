from django import forms
from products.models.product_comment import ProductComment


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['description', 'rating']
