from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView, StockAPIView, StockDetailAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('stocks/', StockAPIView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailAPIView.as_view(), name='stock-detail'),
]