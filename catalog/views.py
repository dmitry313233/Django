from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category


# Create your views here.


class ProductCreateView(LoginRequiredMixin, CreateView):  # form создание
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')  # после выполнения действия сайт перенаправляет нас на домашнюю страницу
    template_name = 'catalog/product_form.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         formset = VersionFormset(self.request.POST, instance=self.object)
    #     else:
    #         formset = VersionFormset(instance=self.object)
    #
    #     context_data['formset'] = formset
    #     return context_data
    #
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductListView(ListView):  #  чтение страницы
    model = Product
    template_name = 'catalog/home.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_update.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_confirm_delete.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    template_name = 'catalog/product_detail.html'  # Создать

    def get_context_data(self, **kwargs):   # Это низкоуровневое кеширование
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'product_list_{self.object.pk}'
            product_list = cache.get(key)
            if product_list is None:
                product_list = self.object.product_set.all()
                cache.set(key, product_list)
        else:
            product_list = self.object.product_set.all()

        context_data['products'] = product_list   #or get_cashed_subjects_for_product(self.object_pk)
        return context_data


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'objects_list': product_list
#     }
#     return render(request, 'catalog/home.html', context)

@login_required
def contacts(request):
    # key = 'category_list'  # Низкоуровневое кеширование в категории дата
    # category_list = cache.get(key)
    # if category_list is None:
    #     category_list = Category.objects.all()
    #     cache.set(key, category_list)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


@login_required
def product(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request, 'catalog/product.html', context)
