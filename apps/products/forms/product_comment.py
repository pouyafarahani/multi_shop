from django import forms
from apps.products.models.product_comment import ProductComment


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['description', 'rating']
