#偏函数的作用是将目标函数的某些默认参数固定住
import functools

def power(x,n=2):
    i=1
    s=1
    while i <=n:
        s = s*x
        i+=1
    print('s=',s)
    return s

power3= functools.partial(power,n = 3)
power3(3)

#创建偏函数的时候，实际上可以使用*args,,**kw两
#个参数,实际上就是给前面的函数对象所使用的
a =[ 2,3,4 ]
print(max(a))

max2=functools.partial(max,10)

print(max2(*a))
