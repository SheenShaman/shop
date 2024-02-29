from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from main.models import Category, Product, Subcategory


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SerializerMethodField()

    @staticmethod
    def get_subcategories(category):
        return SubcategorySerializer(Subcategory.objects.filter(category=category), many=True).data

    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'slug_name', 'category', 'subcategory', 'price', 'image_1', 'image_2', 'image_3')

    @staticmethod
    def get_category(obj):
        return obj.subcategory.category.pk
