#
a = [x*x for x in range(1,11)]
print(a)


#list()函数强制类型转换
b=list(range(1,11))
print(b)


#if...esle..生成
c = [x if x%2==0 else -x for x in range(1,11)]
print(c)

c =[x for x in range(1,11) if x%2==0]
print(c)
