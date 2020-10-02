import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self = self * other
        return self

    def __neg__(self):
        return self * (-1)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        return self + (-other)

    def __isub__(self, other):
        self = self - other
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def normalize(self):
        a = abs(self)
        self.x *= 1 / a
        self.y *= 1 / a
        return self

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
