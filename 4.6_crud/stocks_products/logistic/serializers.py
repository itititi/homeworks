from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ('product', 'quantity', 'price')


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True, source='positions_set')

    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        positions_data = validated_data.pop('positions_set')
        stock = Stock.objects.create(**validated_data)
        for position_data in positions_data:
            product_data = position_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            StockProduct.objects.create(stock=stock, product=product, **position_data)
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions_set')
        positions = instance.positions_set.all()

        instance.address = validated_data.get('address', instance.address)
        instance.save()

        products = {}
        for position in positions:
            products[position.product_id] = position
        for position_data in positions_data:
            product_data = position_data.pop('product')
            product, _ = Product.objects.get_or_create(**product_data)
            if product.id in products:
                pos = products[product.id]
                pos.quantity = position_data.get('quantity', pos.quantity)
                pos.price = position_data.get('price', pos.price)
                pos.save()
            else:
                StockProduct.objects.create(stock=instance, product=product, **position_data)
        return instance