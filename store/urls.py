from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('reviews', views.ReviewViewSet)


urlpatterns = router.urls
