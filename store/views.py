from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.serializers import ProductSerializer, CollectionSerializer
from .models import Product, Collection


# Create your views here.
@api_view(["GET"])
def product_list(request):
    queryset = Product.objects.select_related("collection").all()
    serializer = ProductSerializer(
        queryset,
        many=True,
        # `HyperlinkedRelatedField` requires the request in the serializer context. Add `context={'request': request}` when instantiating the serializer.
        context={"request": request},
    )
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serialized = ProductSerializer(product)
    #     return Response(serialized.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    product = get_object_or_404(Product, pk=id)
    serialized = ProductSerializer(product)
    return Response(serialized.data)


@api_view(["GET"])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serialized = CollectionSerializer(collection)
    return Response(serialized.data)
