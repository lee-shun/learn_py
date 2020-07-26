#过滤器与map类似，但是他会根据序列是否满足函数f的判断来选择保留还是放弃
def is_odd(n):
    return n%2==1

print( list(filter(is_odd,[x for x in range(5)])))
