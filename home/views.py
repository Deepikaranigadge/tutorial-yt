from django.shortcuts import render
from product.models import Product 

def home(request):
    templates = 'index.html'

    product_list = Product.objects.all()

    return render(request, templates, {'products': product_list})

