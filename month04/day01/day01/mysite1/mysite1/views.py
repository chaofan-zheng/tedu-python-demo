from django.http import HttpResponse


# 视图函数
# 参数为请求对象
# 返回值为响应对象
def page_2003(request):
    return HttpResponse('这是编号为2003的页面')


def page_2004(request):
    return HttpResponse('这是编号为2004的页面')


def page_index(request):
    return HttpResponse('<h1>不要找小火箭页面了，我是默认首页</h1>')


def page_num(request, num):
    return HttpResponse('path转换器：这是编号为%s的页面' % num)


def page_data(request, data):
    return HttpResponse('data:%s' % data)


def mymath(request, num1, op, num2):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('运算符有误！')
    result = 0
    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2

    # 测试request对象的使用，从request对象中获取客户端请求的信息
    print(request.method)
    print(request.path_info)

    return HttpResponse('计算结果为%s' % result)


def birtday_view(request, y, m, d):
    return HttpResponse('您的生日为：%s年%s月%s日' % (y, m, d))
