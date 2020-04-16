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
    # This checks that the req is POST, otherwise, an empty form will be rendered
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


def product_render_initial_data(req):
    # Passing this obj to the form as the parameter: initial=initial_data
    # Allow us to set initial data in form fields
    initial_data = {
        'title': 'My awesome title'
    }
    # The following 2 lines allow me to edit a db instance
    # We pass the object that we get, to the form as the instance parameter
    obj = Product.objects.get(id=1)
    form = ProductForm(req.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(req, 'products/product_create.html', context)
