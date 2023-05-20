from django.shortcuts import get_object_or_404, redirect
from ..models.product import ProductModel
from ..forms.product_comment import ProductCommentForm


def rate_comment(request, pk):
    comment_form = ProductCommentForm(request.POST)
    if request.method == 'POST':
        print(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.products = get_object_or_404(ProductModel, pk=pk)
            comment_form.save()
        else:
            print('forme valid nist')
    else:
        print('GET hast dadash')
    return redirect('products:product_Detail', pk=pk)
