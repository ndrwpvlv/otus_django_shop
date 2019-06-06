from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product, Category
from otus_django_shop.settings import CART_SESSION_NAME


class IndexCatalog(View):
    template_path = 'catalog/index.html'

    def get(self, request):
        products = Product.objects.all() or None
        return render(request, self.template_path, {'items': products})


class ItemView(View):
    template_path = 'catalog/product.html'

    def get(self, request, product_id):
        items_count = request.session.get('cart').get(str(product_id)) or None
        item = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_path, {'item': item, 'items_count': items_count})

    def post(self, request, product_id):
        request.session.modified = True
        _id = str(product_id)
        if request.session.get(CART_SESSION_NAME).get(_id):
            request.session[CART_SESSION_NAME][_id] += 1
        else:
            request.session[CART_SESSION_NAME][_id] = 1
        item = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_path, {'item': item, 'items_count': request.session['cart'][_id]})


class CategoryView(View):
    template_path = 'catalog/categories.html'

    def get(self, request, path_name: str):
        category = get_object_or_404(Category, path_name=path_name)
        items = Product.objects.filter(category=category.id).all()
        return render(request, self.template_path, {'items': items, 'category': category})
