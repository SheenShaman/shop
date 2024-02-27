from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.CharField(max_length=100, verbose_name='Slug')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение', **NULLABLE)

    ############# parent = True/False #############

    def __str__(self):
        return self.name

    class Meta:
        ############# вставить категория/подкатегория #############

        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    slug_name = models.CharField(max_length=100, verbose_name='Slug')
    image = models.ImageField(upload_to='category/', verbose_name='Изображение',
                              **NULLABLE)  ############## как сделать в 3х размерах #############
    price = models.FloatField(verbose_name='Цена', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    ############# Подкатегория??? #############

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
