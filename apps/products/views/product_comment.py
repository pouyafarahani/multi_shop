from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from ..models.product import ProductModel
from ..forms.product_comment import ProductCommentForm


def rate_comment(request, pk):
    comment_form = ProductCommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.products = get_object_or_404(ProductModel, pk=pk)
            comment.save()
            messages.success(request, 'Thank you for your comment')
        else:
            messages.warning(request, 'Enter the information correctly')
    return redirect('products:product_Detail', pk=pk)
