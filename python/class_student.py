import types
"""
一个student类
"""


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()


"""
访问限制
"""


class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        # TODO score有效性验证
        self.__score = score


bart2 = Student2('Bart Simpson', 98)
bart2.print_score()
bart2.set_score(95)
bart2.print_score()

#bart2.__name  #非法访问
# print(bart2._Student2__name)   #强制访问私有变量

