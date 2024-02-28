from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.CharField(max_length=100, verbose_name='Slug')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.image}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.CharField(max_length=100, verbose_name='Slug')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.name} {self.image}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.CharField(max_length=100, verbose_name='Slug')
    ############## как сделать в 3х размерах #############
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)
    price = models.FloatField(verbose_name='Цена', **NULLABLE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.name} {self.image}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
