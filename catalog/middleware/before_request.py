from otus_django_shop.settings import CART_SESSION_NAME


class BeforeRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        request.session.modified = True
        if not request.session.get(CART_SESSION_NAME):
            request.session[CART_SESSION_NAME] = {}
        response = self.get_response(request)
        return response
