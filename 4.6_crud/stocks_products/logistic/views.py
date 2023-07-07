from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.prefetch_related('positions_set__product').all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['positions__product']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_qs'] = Product.objects.all()
        return context


class StockDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.prefetch_related('positions_set__product').all()
    serializer_class = StockSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['product_qs'] = ProductAPIView()


def perform_destroy(self, instance):
    instance.positions_set.all().delete()
    instance.delete()
