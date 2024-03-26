from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    produtos = Product.objects.all()

    context = {
        'products': produtos
    }

    return render(request, 'home.html', context)


def product(request, pk):
    product_view = get_object_or_404(Product, pk=pk)

    context = {
        'product': product_view
    }

    return render(request, 'product.html', context)


def contact(request):
    context = {
        'nome': 'Felipe',
        'email': 'felipe@gmail.com'
    }

    return render(request, 'contact.html', context)


def error_404(request, exception):
    return render(request, '404.html', status=404)
