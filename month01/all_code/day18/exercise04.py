# 练习1：推导装饰器返回值与参数
def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        res = func(*args, **kwargs)
        return res

    return wrapper


@verify_permissions
def insert():
    print("插入")
    return True


@verify_permissions
def delete(p1):
    print("删除")
    return False


print(insert())
print(delete(1001))
