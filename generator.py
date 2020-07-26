#列表生成器
#generator可以直接讲列表生成器的【】用（）代替：：：
L = [x*x for x in range(10)]
print(L)
#生成器
g = (x*x for x in range(10))

for n in g:
    print(n)



#如果一个函数中包含关键字yield，那么就是一个生成器了
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

#调用时，先生成一个对象
o = odd()

# print(next(o))
# print(next(o))
# print(next(o))

#调用时，用for n
for n in odd():
    print(n)
