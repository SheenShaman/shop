from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from main.models import Category, Product, Subcategory, Cart, CartItem
from main.paginators import ShopPaginator
from main.permissions import IsOwner

from main.serializers import (CategorySerializer, ProductSerializer, SubcategorySerializer,
                              CartItemSerializer, CartSerializer)


class CategoryListAPIView(generics.ListAPIView):
    """ Просмотр списка Категорий """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = ShopPaginator
    permission_classes = [AllowAny]


class SubcategoryListAPIView(generics.ListAPIView):
    """ Просмотр списка Подкатегорий """
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    permission_classes = [AllowAny]


class ProductListAPIView(generics.ListAPIView):
    """ Просмотр списка Продуктов """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ShopPaginator
    permission_classes = [AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    """ Просмотр, создание, изменение и удаления Корзины """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Просмотр Корзины пользователя """
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Создание Корзины """
        serializer.save(user=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    """ Просмотр, добавление, изменение и удаления Продукта в Корзине """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Просмотр всех Продуктов в Корзине пользователя """
        return self.request.user.cart.items.all()
