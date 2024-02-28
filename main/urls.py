from django.urls import path

from main.apps import MainConfig
from main.views import CategoryListAPIView,SubcategoryListAPIView, ProductListAPIView

app_name = MainConfig.name

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('subcategories/', SubcategoryListAPIView.as_view(), name='subcategories'),
    path('products/', ProductListAPIView.as_view(), name='products')
]
