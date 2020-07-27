#在函数运行时动态改变原本函数的功能的方式
#装饰器就是再次包装
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('现在是：：：')

print(now.__name__)
