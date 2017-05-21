from __future__ import division
from math import sqrt
from math import acos, cos, sin, degrees

class ComplexNumber(object):
    def __init__(self, real, img):
        try:
            real = float(real)
            img = float(img)
        except ValueError:
            print "Enter numbers. Please."
        self.real = real
        self.img = img

    def conjugate(self):
        return ComplexNumber(self.real, -self.img)

    def __repr__(self):
        if self.img < 0:
            return "%s - %si" % (self.real, -self.img)
        elif self.img == 0:
            return "%s" % (self.real)
        else:
            return "%s + %si" % (self.real, self.img)

    def __add__(self, other):
        realpart = self.real + other.real
        imgpart = self.img + other.img
        return ComplexNumber(realpart, imgpart)

    def __sub__(self, other):
        realpart = self.real - other.real
        imgpart = self.img - other.img
        return ComplexNumber(realpart, imgpart)

    def __mul__(self, other):
        realpart = (self.real * other.real) - (self.img * other.img)
        imgpart = (self.img * other.real) + (other.img * self.real)
        return ComplexNumber(realpart, imgpart)

    def abs(self):
        return sqrt(self.real**2 + self.img**2)

    def __truediv__(self, other):
        numerator = self*other.conjugate()
        denominator = (other.abs())**2
        realpart = numerator.real/denominator
        imgpart = numerator.img/denominator
        return ComplexNumber(realpart, imgpart)

    def __pow__(self, num):
        for i in range(num):
            self = self*self
        return self

    def angle(self):
        angle_in_radians = acos(self.real/self.abs())
        angle_in_degrees = degrees(angle_in_radians)
        return angle_in_degrees

    def polarform(self):

