#map 就是所谓的映射，将方法作用到可迭代对象身上
def power(x,n=2):
    i=1
    s=1
    while i <=n:
        s = s*x
        i+=1
    return s

print(power(5,3))

r = map(power,[x for x in range(1,11)])
#由于返回的r是一个惰性序列，需要list()函数转换
print(list(r))


#reduce所使用的函数，必须是有两个参数作为传入值
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
