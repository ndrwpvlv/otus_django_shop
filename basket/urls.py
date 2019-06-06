from django.urls import path

from . import views

urlpatterns = [
    path('', views.BasketView.as_view(), name='basket'),
    path('clean/', views.BasketCleanView.as_view(), name='basket_clean'),
]
