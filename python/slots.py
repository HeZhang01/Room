"""
在实例中动态绑定绑定属性和方法
个人感觉很少使用
"""
from types import MethodType


class Student(object):
    pass

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


# 动态给实例绑定方法
def set_age(self, age):  # 定义一个实例作为实例方法绑定到Student类上
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法

s.set_age(22)  # 调用实例的方法
print(s.age)


s2 = Student()
#  print(s2.age) 报错 实例不存在

#  给class绑定方法


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(89)
print(s.score)

s2.set_score(88)
print(s2.score)


