from django.shortcuts import render

from .models import Product

# Create your views here.


def product_detail_view(request):
    product = Product.objects.get(id=1)
    # context = {
    #     'title': product.title,
    #     'description': product.description
    # }
    context = {
        'product': product
    }
    return render(request, 'product/detail.html', context)
