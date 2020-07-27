from types import MethodType

class Student(object):
    pass

s1=Student()


#给实例绑定属性
s1.name = 'Mac'
print(s1.name)


#给实例绑定方法
def set_age(self,age):
    self.age = age
    print("set age to:",self.age)

s1.set_age = MethodType(set_age,s1)

s1.set_age(11)


#给class绑定方法
def set_score(self,score):
    self.score = score
    print("set score to:",self.score)

Student.set_sc = set_score

s2 = Student()

s2.set_sc(100)

#想要限制实例添加属性的种类，可以使用__solt__变量

class Teacher(object):
    __slots__ = ('name','age')

teacher1 = Teacher()
teacher1.name = 'lee-shun'
teacher1.score = 100
