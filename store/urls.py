from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("products/<int:id>/", views.ProductDetail.as_view()),
    path("collections/", views.collection_list),
    # You may have failed to include the related model in your API, or incorrectly configured the `lookup_field` attribute on this field.
    # Convert id to pk in the path
    path("collections/<int:pk>/", views.collection_detail, name="collection-detail"),
]
