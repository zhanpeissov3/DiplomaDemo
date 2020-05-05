from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'icon', 'price', 'content', 'photo', 'publish', 'created', 'updated']
    list_filter = ['created', 'updated', 'price']
    list_editable = ['price', ]
    search_fields = ('title', 'content')

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Service, ServiceAdmin)
