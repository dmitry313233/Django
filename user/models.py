from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    number_phone = models.CharField(max_length=50, verbose_name='номер телефона')
    country = models.CharField(max_length=100, verbose_name='страна')
    avatar = models.ImageField(upload_to='user/', verbose_name='аватар')
    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField("active", default=False, help_text=(
        "Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts."
    )
                                    )
    cod = models.CharField(verbose_name='Код', null=True, blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
