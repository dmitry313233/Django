from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from bloc_record.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'body',)
    success_url = reverse_lazy('bloc_record:blog_record_list')
    template_name = 'bloc_record/blog_record_create.html'

    def form_valid(self, form):   # при создании динамически формировать slug name для заголовка;
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):  #  чтение страницы
    model = Blog  #
    template_name = 'bloc_record/blog_record_list.html'
    success_url = reverse_lazy('bloc_record:blog_record_list')

    def get_queryset(self, *args, **kwargs):   # выводить в список статей только те, которые имеют положительный признак публикации;
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publishing_mark=True)
        return queryset



class BlogDetailView(DetailView): # счетчик
    model = Blog

    def get_object(self, queryset=None):   # при открытии отдельной статьи увеличивать счетчик просмотров;
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):  # редактирование
    model = Blog
    fields = ('title', 'body',)
    #success_url = reverse_lazy('bloc_record:blog_update')
    template_name = 'bloc_record/blog_update.html'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)



    def get_success_url(self):
        return reverse('bloc_record:blog_update', args=[self.kwargs.get('pk'),])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('bloc_record:blog_record_list')
    template_name = 'bloc_record/blog_confirm_delete.html'
