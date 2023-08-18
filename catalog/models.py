from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='название')
    discription = models.TextField(verbose_name='описание')
    avatar = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='аватар')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Products'
        ordering = ('last_modified_date', 'name',)

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    discription = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)