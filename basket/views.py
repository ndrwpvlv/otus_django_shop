from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.forms.models import model_to_dict
from catalog.models import Product
from otus_django_shop.settings import CART_SESSION_NAME


class BasketView(View):
    template_path = 'basket/index.html'

    def get(self, request):
        cart = request.session.get(CART_SESSION_NAME) or None
        receipt = None
        total = None
        if cart:
            _ids = [int(_id) for _id in cart]
            items = {model_to_dict(row)['id']: model_to_dict(row) for row in Product.objects.filter(pk__in=_ids)}
            receipt = [{
                'title': items[_id]['title'],
                'count': cart[str(_id)],
                'single_price': float(items[_id]['price']),
                'total_price': float(items[_id]['price']) * float(cart[str(_id)]),
            } for _id in _ids]
            total = sum([p['total_price'] for p in receipt])
        return render(request, self.template_path, {'receipt': receipt, 'total': total})


class BasketCleanView(View):

    def get(self, request):
        request.session[CART_SESSION_NAME] = {}
        return redirect('/basket/')
