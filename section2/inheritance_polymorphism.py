"""
this is the animal class, basic class!!
"""


class Animal(object):
    def run(self):
        print("Animal is running")


class Cat(Animal):
    pass


class Dog(Animal):
    def run(self):
        print("Dog is running")


dog1 = Dog()
dog1.run()

cat1 = Cat()
cat1.run()


"""
python的函数传入不管类型如何，所以只要有一个run()方法，double_run()
就可以被成功调用！！！
动态语言的”鸭子类型“
"""


def double_run(animal):
    animal.run()
    animal.run()


double_run(dog1)


class Hello(object):
    def run(self):
        print("hello-->run")


hel = Hello()
double_run(hel)
