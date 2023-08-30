# Generated by Django 4.2.4 on 2023-08-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='.../', verbose_name='аватар')),
                ('data_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('publishing_mark', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('count_views', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
        ),
    ]
