from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from ..models.product import ProductModel
from ..forms.product_comment import ProductCommentForm


@cache_page(600)  # 600sec == 10 min
def rate_comment(request, pk):
    comment_form = ProductCommentForm(request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.products = get_object_or_404(ProductModel, pk=pk)
            comment.save()
        else:
            pass
    return redirect('products:product_Detail', pk=pk)
