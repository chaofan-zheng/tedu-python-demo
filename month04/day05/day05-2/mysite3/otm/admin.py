from django.contrib import admin
from .models import *


# Register your models here.
class PublisherManager(admin.ModelAdmin):
    list_display = ['id', 'name']


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


admin.site.register(Publisher, PublisherManager)
admin.site.register(Book, BookManager)
