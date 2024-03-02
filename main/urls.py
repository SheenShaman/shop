from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.apps import MainConfig
from main.views import CategoryListAPIView, ProductListAPIView, SubcategoryListAPIView, CartViewSet, CartItemViewSet

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('subcategories/', SubcategoryListAPIView.as_view(), name='subcategories'),
    path('products/', ProductListAPIView.as_view(), name='products'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
