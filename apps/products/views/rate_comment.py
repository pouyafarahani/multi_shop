from django.shortcuts import get_object_or_404, redirect

from products.models.product_comment import *


def rate_comment(request, comment_id):
    comment = get_object_or_404(ProductComment, id=comment_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment.rating = rating
        comment.author = request.user
        comment.save()
    return redirect('products:product_Detail', product_id=comment.products.id)
