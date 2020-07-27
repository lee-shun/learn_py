class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

shun = Student('shun',100)

shun.print_score()

#错误做法，生将私有成员赋值，不成功，私有成员未更改
shun.__name = 'lee-shun'
print(shun.__name)

shun.print_score()

