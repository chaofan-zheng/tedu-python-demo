from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book


# Create your views here.
def all_book(request):
    all_book = Book.objects.all()
    return render(request, 'bookstore/all_book.html', locals())


def add_book(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':

        # 1 获取客户端提交的表单数据
        title = request.POST['title']  # 表单数据
        pub = request.POST['pub']
        price = request.POST['price']
        market_price = request.POST['market_price']
        print(title, pub, price, market_price)
        # 2 使用这些数据，在后端的数据库中创建一条记录
        Book.objects.create(title=title, pub=pub,
                            price=price, market_price=market_price)

        # 添加，重定向到列表页
        return HttpResponseRedirect('/bookstore/all_book')




def update_book(request, bid):
    # 1.先从数据库中读取要修改的图书
    try:
        book = Book.objects.get(id=bid)
    except:
        return HttpResponse('图书编号错误！')
    # 2.处理get/post请求
    if request.method == 'GET':
        return render(request,
                      'bookstore/update_book.html',
                      locals())
    elif request.method == 'POST':
        market_price = request.POST['market_price']
        book.market_price = market_price
        book.save()
        # 修改后，重定向到列表页
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    # 首先从查询字符串中获取图书编号
    bid = request.GET.get('bid')
    # 然后 获取要删除的对象
    try:
        book = Book.objects.get(id=bid)
    except:
        return HttpResponse('图书编号错误！')
    book.delete()

    # 删除后，重定向到列表页
    return HttpResponseRedirect('/bookstore/all_book')