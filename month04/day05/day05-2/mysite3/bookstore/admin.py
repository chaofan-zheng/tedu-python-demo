from django.contrib import admin
from .models import Book


# Register your models here.
#  创建一个模型管理器类，用来管理Book模型类
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['id', 'title']
    list_filter = ['pub']
    search_fields = ['title', 'price']
    list_editable = ['market_price']


# 注册
admin.site.register(Book, BookManager)
