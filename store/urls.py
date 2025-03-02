from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)

product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

urlpatterns = router.urls + product_router.urls

# [
#     <URLPattern '^products/$' [name='product-list']>,
#     <URLPattern '^products/(?P<pk>[^/.]+)/$' [name='product-detail']>,
#     <URLPattern '^collections/$' [name='collection-list']>,
#     <URLPattern '^collections/(?P<pk>[^/.]+)/$' [name='collection-detail']>
# ]
