from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'key': 'Django Web Framework!',
        'outro': 'Django é massa',
        'produtos': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    produto = Product.objects.get(id=pk)
    context = {'produto': produto}
    return render(request, 'produto.html', context)
