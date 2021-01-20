from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Note
# 登录认证的装饰器
def login_check(fn):
    def wrap(request, *args, **kwargs):
        # 在session没有登录信息
        if 'uname' not in request.session or 'uid' not in request.session:
            # 重定向到登录url
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)

    return wrap


# Create your views here.
@login_check
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        # 1 获取数据
        title = request.POST['title']
        content = request.POST['content']
        uid = request.session['uid']
        # 2 数据入库
        Note.objects.create(title=title,
                            content=content,
                            user_id = uid)
        return  HttpResponse('添加笔记成功！')


@login_check
def list_view(request):
    username = request.session['uname']
    uid = request.session['uid']
    notes = Note.objects.filter(user_id=uid)
    return render(request,'note/list_note.html',locals())
