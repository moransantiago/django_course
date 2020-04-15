from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# HOW TO MAKE A DJANGO FORM WITH RAW HTML
# def product_create_view(req):
#     form = RawProductForm(req.POST or None)
#     if req.method == 'POST':
#         form = RawProductForm(req.POST or None)
#         if form.is_valid():
#             form.save()
#             Product.objects.create(**form.cleaned_data)

#     context = {
#         'form': form
#     }
#     return render(req, 'products/product_create.html', context)


def product_create_view(req):
    form = ProductForm(req.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # Re render the form

    context = {
        'form': form
    }
    return render(req, 'products/product_create.html', context)


def product_detail_view(req):
    product = Product.objects.get(id=1)
    context = {
        'product': product
    }
    return render(req, 'products/product_detail.html', context)
