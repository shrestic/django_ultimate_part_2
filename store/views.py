from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.serializers import ProductSerializer, CollectionSerializer
from .models import Product, Collection


# Create your views here.
@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(
            queryset,
            many=True,
            # `HyperlinkedRelatedField` requires the request in the serializer context. Add `context={'request': request}` when instantiating the serializer.
            context={"request": request},
        )
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        # Using `raise_exception=True` will raise a `ValidationError` exception if the data is invalid.
        # Using 'raise_exception=True' will replace if-else block
        serializer.is_valid(raise_exception=True)
        # Note: `validated_data` contains the validated data but does not cover object-level validation.
        # If you need to perform object-level validation, you can override the `validate()` method on Serializer class.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT"])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serialized = ProductSerializer(product)
        return Response(serialized.data)
    elif request.method == "PUT":
        serialized = ProductSerializer(product, data=request.data, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data)


@api_view(["GET"])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serialized = CollectionSerializer(collection)
    return Response(serialized.data)
