from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexCatalog.as_view(), name='index_catalog'),
    path('<int:product_id>/', views.ItemView.as_view(), name='single_product'),
    path('<str:path_name>/', views.CategoryView.as_view(), name='categories'),
]
