from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product


def product_list_view(req):
    queryset = Product.objects.all()  # All products
    context = {
        'product_list': queryset
    }

    return render(req, 'products/product_list.html', context)

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
    # This checks that the req is POST, otherwise, an empty form will be rendered
    form = ProductForm(req.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # Re render the form

    context = {
        'form': form
    }

    return render(req, 'products/product_create.html', context)


def product_detail_view(req, id):
    # This allows to throw an HttpResponseError if the obj wasn't found
    # get_object_or_404 recieves: (MODEL, ID)

    prod = get_object_or_404(Product, id=id)
    context = {
        'product': prod
    }

    # Another way:
    # try:
    #     prod = Product.objects.get(id=id)
    #     context = {
    #         'product': prod
    #     }
    # except Product.DoesNotExist:
    #     raise Http404

    return render(req, 'products/product_detail.html', context)


def product_update_view(req, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(req.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }

    return render(req, 'products/product_create.html', context)


def product_delete_view(req, id):
    prod = get_object_or_404(Product, id=id)
    if req.method == 'POST':
        prod.delete()

        return redirect('../../')
    context = {
        'product': prod
    }

    return render(req, 'products/product_delete.html', context)
