print(type(123))

#实例属性以及类属性
class Student(object):
    def __init__(self, name):
        self.name = name

#给实例绑定属性
s = Student('Bob')
s.score = 90

#类属性就是在类中直接定义属性，同名的属性，实例的会覆盖掉类的属性
