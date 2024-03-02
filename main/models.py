from django.db import models

from django.contrib.auth.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.SlugField(max_length=100, unique=True)
    image_1 = models.ImageField(upload_to='category/', verbose_name='Изображение размера 1', **NULLABLE)
    image_2 = models.ImageField(upload_to='category/', verbose_name='Изображение размера 2', **NULLABLE)
    image_3 = models.ImageField(upload_to='category/', verbose_name='Изображение размера 3', **NULLABLE)
    price = models.FloatField(verbose_name='Цена')

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
