from django import template
from config import settings
register = template.Library()



@register.filter()
def mymedia(val):
    if val:
        return f'{settings.MEDIA_URL}{val}'
    else:
        return f'{settings.MEDIA_URL}products/img_1.png'