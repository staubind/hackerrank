import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def __add__(self, no):
        real = self.real + no.real
        imag = self.imag + no.imag
        return Complex(real, imag)
        
    def __sub__(self, no):
        real = self.real - no.real
        imag = self.imag - no.imag
        return Complex(real, imag)
    
    def __mul__(self, no):
        real = self.real * no.real - self.imag * no.imag
        imag = self.real * no.imag + self.imag * no.real
        return Complex(real, imag)
    
    def __truediv__(self, no):
        try:
            real = (self.real * no.real + self.imag * no.imag) / (no.real**2 + no.imag**2)
            imag = (self.imag * no.real - self.real * no.imag) / (no.real**2 + no.imag**2)
        except ZeroDivisionError:
            return None
        return Complex(real, imag)
        
    def mod(self):
        return Complex((self.real**2 + self.imag**2)**.5, 0)
        
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':