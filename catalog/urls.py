from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_catalog, name='index_catalog'),
    path('<int:product_id>/', views.get_product, name='single_product'),
    path('<str:path_name>/', views.get_category, name='categories'),
]
