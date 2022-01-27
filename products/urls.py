from django.urls import path, include
from .views import ProductList, CategoryList, SellerList, ProductListAPIVIew

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products-filter/', ProductListAPIVIew.as_view()),
    path('categories/', CategoryList.as_view()),
    path('sellers/', SellerList.as_view())
]
