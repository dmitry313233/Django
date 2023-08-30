from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='slug')  #
    body = models.TextField(verbose_name='содержимое', null=True, blank=True)
    avatar = models.ImageField(upload_to='.../', null=True, blank=True, verbose_name='аватар')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    publishing_mark = models.BooleanField(default=True, verbose_name='опубликовано')  #
    count_views = models.IntegerField(default=0, verbose_name='просмотры')  #

    def __str__(self):
        return f'{self.title}, {self.count_views}'


class Meta:
    verbose_name = 'блоговая запись'
    verbose_name_plural = 'блоговые записи'