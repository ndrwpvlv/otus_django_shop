from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def index_catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'items': products})


def get_product(request, product_id):
    item = get_object_or_404(Product, pk=product_id)
    return render(request, 'catalog/product.html', {'item': item})


def get_category(request, path_name: str):
    category = get_object_or_404(Category, path_name=path_name)
    items = Product.objects.filter(category=category.id).all()
    return render(request, 'catalog/categories.html', {'items': items, 'category': category})
