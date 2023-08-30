from django.contrib import admin

from bloc_record.models import Blog


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count_views')
    search_fields = ('title',)
    ordering = ('pk',)