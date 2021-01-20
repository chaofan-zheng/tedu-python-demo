from django.contrib import admin
from .models import *


# Register your models here.
class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name']


class BookManager(admin.ModelAdmin):
    # 不能有authors，因为两者不存在直接关联
    #list_display = ['id', 'title','authors']
    list_display = ['id', 'title']


admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
