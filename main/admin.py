from django.contrib import admin

from main.models import Category, Product, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_name', 'image')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_name', 'image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug_name', 'image_1', 'image_2', 'image_3', 'price', 'subcategory')
