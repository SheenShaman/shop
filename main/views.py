from rest_framework import generics

from main.models import Category, Subcategory, Product
from main.paginators import ShopPaginator

from main.serializers import CategorySerializer, SubcategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
    """ Просмотр списка Категорий """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = ShopPaginator


class SubcategoryListAPIView(generics.ListAPIView):
    """ Просмотр списка Подкатегорий """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()


class ProductListAPIView(generics.ListAPIView):
    """ Просмотр списка Продуктов """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ShopPaginator
