from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    # GenericView requires pk not id
    path("products/<int:pk>/", views.ProductDetail.as_view()),
    path("collections/", views.CollectionList.as_view()),
    # You may have failed to include the related model in your API, or incorrectly configured the `lookup_field` attribute on this field.
    # Convert id to pk in the path
    path("collections/<int:pk>/", views.CollectionDetail.as_view(), name="collection-detail"),
]
