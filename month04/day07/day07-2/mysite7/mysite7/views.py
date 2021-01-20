import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(100)
def test_cache(request):
    t1 = time.time()
    print('-------views in--------')
    # 模拟耗时操作(可以是复杂的查询，也可以复杂的计算)
    time.sleep(3)
    return HttpResponse('time is %s' % t1)


def test_mw(request):
    print('my view in')
    return HttpResponse('my middlware view!')
