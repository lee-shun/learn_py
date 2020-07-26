#高阶函数就是以函数为输入对象的函数
f =abs
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,-6,f))
