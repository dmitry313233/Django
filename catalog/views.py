from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/product.html', context)



# Может быть мы не загрузили файл static?
# Может быть {%block%} ставится в base а не в products с 6:20?  1111
# Изменения в base не меняют страницу