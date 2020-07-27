class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int!')
        if value < 0 or value > 100:
            raise ValueError("score must be in 1 to 100")
        self._score = value
        print("set score to:", self._score)


"""
注意：这里的s1.score并不是单纯的属性绑定，而是使用@proptery给函数做出来的
score是方法，虽然很像动态的属性！！！！
"""

s1 = Student()
s1.score = 60
print(s1.score)
s1.score = 101
