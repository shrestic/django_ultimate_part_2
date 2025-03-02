from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)
urlpatterns = router.urls

# [
#     <URLPattern '^products/$' [name='product-list']>,
#     <URLPattern '^products/(?P<pk>[^/.]+)/$' [name='product-detail']>,
#     <URLPattern '^collections/$' [name='collection-list']>,
#     <URLPattern '^collections/(?P<pk>[^/.]+)/$' [name='collection-detail']>
# ]
