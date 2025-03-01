from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from decimal import Decimal
from store.models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection =CollectionSerializer()
    collection = HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name="collection-detail",
    )

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.2)
