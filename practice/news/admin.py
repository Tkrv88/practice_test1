from django.contrib import admin
from .models import News, Type

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'short_description',
        'full_description',
        'type'
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color'
    )

admin.site.register(News, NewsAdmin)
admin.site.register(Type, TypeAdmin)
