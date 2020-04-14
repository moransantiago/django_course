from django.shortcuts import render

from .forms import ProductForm

from .models import Product

# Create your views here.


# HOW TO MAKE A DJANGO FORM WITH RAW HTML
# def product_create_view(req):
#     if req.method == 'POST':
#         title = req.POST['title']
#         description = req.POST['description']
#         price = req.POST['price']
#         Product.objects.create(title=title, description=description, price=price)
#     context = {}
# return render(req, 'products/product_create.html', context)


# HOW TO MAKE A DJANGO FORM WITH AUTO VALIDATION
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    product = Product.objects.get(id=1)
    # context = {
    #     'title': product.title,
    #     'description': product.description
    # }
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)
