# abs是一个内置函数,如果输入complex,返回模

from math import hypot


class Vector:
# 总共六个特殊方法,除了__init__外,其他都不会在这个类自身的代码中使用
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# python 有内置的repr函数, 将对象以字符串的形式表示出来以便辨认
# repr是通过__repr__这个特殊方法来得到一个对象的字符串表示形式的
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


print(repr("hi"))
print(str("hi"))
v = Vector(2, 4)
v1 = Vector(2, 1)
print("add: ", v + v1)
print("abs: ", abs(v))
print("bool: ", bool(v))
print("mul: ", v * 3)
print("repr: ", repr(v))

