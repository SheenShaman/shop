from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Product
from main.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """ ViewSet for Category """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
