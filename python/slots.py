"""
在实例中动态绑定绑定属性和方法
个人感觉很少使用
"""


class Student(object):
    pass

s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)





