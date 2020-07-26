#返回一个函数，真正调用这个返回的函数时候，真正的逻辑才会被执行
def lazy_sum(*args):
    def sum_num():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum_num

f = lazy_sum(1,2,3,4)
print(f())

#闭包:当函数作为返回值返回时，函数的局部变量还可以被新函数所引用，而且函数
#被返回的时候，实际上是返回了算法，算法的结果要在函数被调用时利用当时
#的变量计算
