#!usr/bin/env python3
"""
Create a class Rational whose instances are rational numbers. A new rational number can be created with the call to
the class. For example, the call r=Rational(1,4) creates a rational number “one quarter”. Make the instances support
the following operations: + - * / < > == with their natural behaviour. Make the rationals also printable so that from
the printout we can clearly see that they are rational numbers.
"""


class Rational(object):
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"{self.num}/{self.denum}"

    def __add__(self, other):
        up = (other.denum * self.num) + (self.denum * other.num)
        down = other.denum * self.denum
        return Rational(up, down)

    def __sub__(self, other):
        up = (other.denum * self.num) - (self.denum * other.num)
        down = other.denum * self.denum
        return Rational(up, down)

    def __mul__(self, other):
        up = self.num * other.num
        down = self.denum * other.denum
        return Rational(up, down)

    def __truediv__(self, other):
        up = self.num * other.denum
        down = self.denum * other.num
        return Rational(up, down)

    def __eq__(self, other):
        if float(self.num / self.denum) == float(other.num / other.denum):
            return True
        else:
            return False

    def __gt__(self, other):
        if float(self.num / self.denum) > float(other.num / other.denum):
            return True
        else:
            return False


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)

    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()