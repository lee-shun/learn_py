#位置参数
def power(x):
    return x*x


print('power={}'.format(power(5)))

#默认参数


def power2(x, n=2):
    s = 1
    for i in range(n):
        i += 1
        s = s*x
    return s


print('power2={}'.format(power2(6)))

#默认参数的坑


def add_end(L=[]):
    L.append('endd')
    return L


print(add_end())
"""
当函数定义的时候，动态语言已经将L指向了“[]”这块空间，下一次调用
的时候，他不会重新计算所调用的函数，只是使用最开始函数所开辟的，
如果这里的内容被更更改了的话，下一次调用就会使用更改后的值：：
动态语言！！！！！！

#所以，默认参数需要指向不变数值
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
"""
print(add_end())


#可变参数
#组装成为一个tuple
def cal_sum(*number):
    s = 0
    for n in number:
        s = s+n
    return s


print(cal_sum(1, 1, 1, 22, 3))

# 如果已经有一个lisst或者tuple，则可以拆开
l1 = [1, 1, 2, 4, 5, ]
print(cal_sum(*l1))


#关键字参数-->组装成为dict
def person(name, **kw):
    print("naaaame:", name, "other:", kw)


person('Adam',  gender='M', job='Engineer')


#命名关键字参数
def person2(name,*,city,job):
    print(name,city,job)


person2('lee',city='beijing',job='hot')


#参数组合
def f1(a,b,c=0,*args,v,**kw):
    #必选参数、默认参数、可变参数、命名关键字参数以及关键字参数
    print('必选参数a={},b={}'.format(a,b))
    print('默认参数c={}'.format(c))
    print('可变参数args={}'.format(args))
    print('命名关键字参数v={}'.format(v))
    print('关键字参数kw={}'.format(kw))


f1(1,2,3,6,7,8,v=9,kw1=10,kw2='12')
